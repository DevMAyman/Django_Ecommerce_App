from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem
from rest_framework import generics, mixins, viewsets
from rest_framework import filters


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    filter_set_fields = ["order_creation_date"]


class OrderItemView(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        queryset = super().get_queryset()
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if min_price is not None and max_price is not None:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        elif min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        elif max_price is not None:
            queryset = queryset.filter(price__lte=max_price)

        return queryset
