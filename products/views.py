from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status, filters,viewsets
from rest_framework.decorators import api_view
from .models import Product,ProductImage,Rating
from .serializers import ProductSerializer,ProductImageSerializer,RatingSerializer

@api_view(['GET'])
def GetAllProducts(request):
       
    #GET
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

        # Apply the search filter
        queryset = filters.SearchFilter().filter_queryset(request, queryset, view=GetAllProducts)

        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
@api_view(['GET'])
def getProductById(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data,status.HTTP_200_OK)
    

class Viewset_Ratings(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer