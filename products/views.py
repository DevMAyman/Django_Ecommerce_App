from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, filters,viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,ProductImage
from .serializers import ProductSerializer,ProductImageSerializer

class Viewset_Products(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','stock','price','category__name']

class Viewset_ProductImages(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer