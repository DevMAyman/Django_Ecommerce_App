from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem
from rest_framework import generics, mixins, viewsets, permissions
from rest_framework import filters
from user import authentication
from datetime import datetime, timezone


  

class OrderView(viewsets.ModelViewSet):
    authentication_classes=(authentication.CustomUserAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    filter_set_fields = ["order_creation_date"]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        order_creation_date = instance.order_creation_date
        if (timezone.now() - order_creation_date).days > 4:
            return Response({"error": "Cannot update orders older than 4 days."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        order_creation_date = instance.order_creation_date
        if (datetime.now(timezone.utc) - order_creation_date).total_seconds() > 5*60:
            return Response({"error": "Cannot delete orders older than 4 days."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)



class OrderItemView(viewsets.ModelViewSet):
    authentication_classes=(authentication.CustomUserAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)
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
