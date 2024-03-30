from django.shortcuts import render
from rest_framework import status, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
from products.models import Product
from products.serializers import ProductSerializer
# Create your views here.
@api_view(['GET','Post'])
def GetCategories(request):
    #GET
    if request.method=='GET':
        categories=Category.objects.all()
        serializer=CategorySerializer(categories,many=True)
        return Response(serializer.data,status.HTTP_200_OK)

@api_view(['GET'])
def GetCategoryProducts(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        return Response({"detail": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

    products = Product.objects.filter(category=category)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)    