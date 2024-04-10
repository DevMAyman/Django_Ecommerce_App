from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ['user'] 

    def validate(self, data):
        total_price = data.get("total_price")

        if total_price is not None and total_price < 0:
            raise serializers.ValidationError("Total price can not be negative")

        return data


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        product_data = instance.product
        product_serializer = ProductSerializer(product_data)
        representation['product'] = product_serializer.data
        return representation