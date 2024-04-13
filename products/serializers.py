from rest_framework import serializers
from .models import Product,ProductImage,Rating



class ProductSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.SerializerMethodField()
    class Meta:
        model=Product
        fields='__all__'
    def get_thumbnail_url(self, obj):
        return obj.thumbnail.url

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        fields='__all__'              

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields='__all__'        