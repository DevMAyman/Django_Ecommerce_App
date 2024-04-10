from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem, Product
from rest_framework import viewsets, permissions
from rest_framework import filters, status
from user import authentication
from datetime import datetime, timezone
from products.serializers import ProductSerializer
from django.db.models import Q, Prefetch
from rest_framework.decorators import action


class OrderView(viewsets.ModelViewSet):
    # authentication_classes = (authentication.CustomUserAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        user = self.request.query_params.get("user")

        if user:
            queryset = queryset.filter(Q(user=user))

        queryset = queryset.prefetch_related(
            Prefetch("items", queryset=OrderItem.objects.all(), to_attr="order_items")
        )

        return queryset

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["POST"])
    def cancel_order(self, request, pk=None):
        order = self.get_object()
        if order.status == "Delivered" or order.status == "Canceled":
            return Response(
                {"message": "Order cannot be canceled"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        order.status = "Canceled"
        order.save()
        return Response({"message": "Order cancelled successfully"})


# class OrderView(viewsets.ModelViewSet):
#     # authentication_classes = (authentication.CustomUserAuthentication,)
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer


# def update(self, request, *args, **kwargs):
#     instance = self.get_object()
#     order_creation_date = instance.order_creation_date
#     if (timezone.now() - order_creation_date).days > 4:
#         return Response(
#             {"error": "Cannot update orders older than 4 days."},
#             status=status.HTTP_403_FORBIDDEN,
#         )
#     return super().update(request, *args, **kwargs)

# def destroy(self, request, *args, **kwargs):
#     instance = self.get_object()
#     order_creation_date = instance.order_creation_date
#     if (datetime.now(timezone.utc) - order_creation_date).total_seconds() > 5 * 60:
#         return Response(
#             {"error": "Cannot delete orders older than 4 days."},
#             status=status.HTTP_403_FORBIDDEN,
#         )
#     return super().destroy(request, *args, **kwargs)


class OrderItemView(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        for orderitem_data in serializer.data:
            print(orderitem_data)
            product_id = orderitem_data["product"]["id"]
            product = Product.objects.get(pk=product_id)
            product_serializer = ProductSerializer(product)
            orderitem_data["product"] = product_serializer.data


        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Retrieve the Product using the product_id field from the OrderItem
        product = Product.objects.get(pk=instance.product_id)
        product_serializer = ProductSerializer(product)
        data = serializer.data
        data["product"] = product_serializer.data

        return Response(data)

