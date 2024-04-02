from django.shortcuts import render
from rest_framework import status, filters,viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
# Create your views here.
@api_view(['GET'])
def GetAllCategories(request):
    #GET
    if request.method=='GET':
        categories=Category.objects.all()
        serializer=CategorySerializer(categories,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
