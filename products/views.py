from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,ProductImage
from .serializers import ProductSerializer,ProductImageSerializer
# Create your views here.
@api_view(['GET','Post'])
def GetProducts(request):
    #GET
    if request.method=='GET':
        proucts=Product.objects.all()
        serializer=ProductSerializer(proucts,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET','PATCH','DELETE'])
def FBV_pk(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data,status.HTTP_200_OK)
        
    # PATCH
    elif request.method == 'PATCH':
        serializer = ProductSerializer(product, data= request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        product.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)



