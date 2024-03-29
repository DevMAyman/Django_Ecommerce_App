from rest_framework import serializers
from .models import Product,ProductImage,Category



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        fields=['pk','images','image']                