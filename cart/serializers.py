from rest_framework import serializers
from cart.models import Cart , Cart_item , Wishlist

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_item
        fields = '__all__'

class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'