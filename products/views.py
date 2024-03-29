from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,Category,ProductImage
from .serializers import ProductSerializer,ProductImageSerializer,CategorySerialzer
# Create your views here.
@api_view(['GET','Post'])
def GetProducts(request):
    #GET
    if request.method=='GET':
        proucts=Product.objects.all()
        serializer=ProductSerializer(proucts,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    



def index(request):
    return HttpResponse('hello world')
