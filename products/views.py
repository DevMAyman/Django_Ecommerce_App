from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, filters, viewsets, permissions
from rest_framework.decorators import api_view
from .models import Product, ProductImage, Rating
from .serializers import ProductSerializer, ProductImageSerializer, RatingSerializer
from user import authentication
from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 100

@api_view(['GET'])
def GetAllProducts(request):
    # GET
    if request.method == 'GET':
        queryset = Product.objects.all()

        category = request.GET.get('category', None)
        if category:
            queryset = queryset.filter(category__name__icontains=category)

        rating = request.GET.get('rating', None)
        if rating:
            queryset = queryset.filter(rating__icontains=rating)

        price = request.GET.get('price', None)
        if price:
            queryset = queryset.filter(price__icontains=price)

        name = request.GET.get('name', None)
        if name:
            queryset = queryset.filter(name__icontains=name)

        # Check if the request wants products ordered by rating
        order_by_rating = request.GET.get('order_by_rating', None)
        if order_by_rating:
            if order_by_rating.lower() == 'asc':
                queryset = queryset.order_by('rating')
            elif order_by_rating.lower() == 'desc':
                queryset = queryset.order_by('-rating')

        # Check if the request wants products ordered by price
        order_by_price = request.GET.get('order_by_price', None)
        if order_by_price:
            if order_by_price.lower() == 'asc':
                queryset = queryset.order_by('price')
            elif order_by_price.lower() == 'desc':
                queryset = queryset.order_by('-price')

        # Apply the search filter
        queryset = filters.SearchFilter().filter_queryset(request, queryset, view=GetAllProducts)

        # Apply pagination
        paginator = ProductPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        
        serializer = ProductSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def getProductById(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # GET
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Viewset_Ratings(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

@api_view(['GET', 'POST', 'PUT'])
def manageUserRating(request, user_id, product_id):
    try:
        rating = Rating.objects.get(user=user_id, product=product_id)
    except Rating.DoesNotExist:
        rating = None

    if request.method == 'GET':
        if rating:
            serializer = RatingSerializer(rating)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Rating not found"}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST' or request.method == 'PUT':
        user_rating = request.data.get('user_rating')

        if not user_rating:
            return Response({"message": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

        if rating:
            rating.user_rating = user_rating
            rating.save()
        else:
            rating = Rating.objects.create(user=user_id, product=product_id, user_rating=user_rating)
            rating.save()

        serializer = RatingSerializer(rating)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def getRatingsByProduct(request, product_id):
    try:
        ratings = Rating.objects.filter(product_id=product_id)
    except Rating.DoesNotExist:
        return Response({"message": "Ratings not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = RatingSerializer(ratings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getRatingsByUser(request, user_id):
    try:
        ratings = Rating.objects.filter(user_id=user_id)
    except Rating.DoesNotExist:
        return Response({"message": "Ratings not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = RatingSerializer(ratings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def GetProductsImages(request, product_id):
    # GET
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        images = ProductImage.objects.filter(product=product)
        serializer = ProductImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
