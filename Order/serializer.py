from rest_framework import serializers
from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    def validate(self, data):
        total_price = data.get("total_price")

        if total_price is not None and total_price < 0:
            raise serializers.ValidationError("Total price can not be negative")

        return data


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

    def validate(self, data):
        price = data.get("price")
        quantity = data.get("quantity")

        if price is not None and price < 0:
            raise serializers.ValidationError("Price can not be negative")

        if quantity is not None and quantity < 0:
            raise serializers.ValidationError("Quantity can not be less than zero")

        return data
