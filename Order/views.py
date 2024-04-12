from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem, Product, User
from rest_framework import viewsets, permissions
from rest_framework import filters, status
from user import authentication
from datetime import datetime, timezone
from products.serializers import ProductSerializer
from django.db.models import Q, Prefetch
from rest_framework.decorators import action
from django.db import transaction

class OrderView(viewsets.ModelViewSet):
    authentication_classes=(authentication.CustomUserAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user')
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        order_items_data = request.data.pop('items', [])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        with transaction.atomic():
            order_instance = serializer.save(user=user)  

            for item_data in order_items_data:
                
                item_data['order_id'] = order_instance.id
                order_item_serializer = OrderItemSerializer(data=item_data)
                order_item_serializer.is_valid(raise_exception=True)
                order_item_serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# {
#   "total_price": 2000,
#   "shipment_id": 1,
#   "order_creation_date":"2024-04-12T22:24:00Z",
#   "delivery_date": "2024-04-30T22:24:00Z",
#   "status": "pending",
#   "user": 1,
#   "items": [
#     {
#       "quantity": 1,
#       "price": 1000,
#       "product": 1
#     },
#     {
#       "quantity": 1,
#       "price": 2000,
#       "product": 2
#     }
#   ]
# }


# class OrderView(viewsets.ModelViewSet):
#     authentication_classes=(authentication.CustomUserAuthentication,)
#     permission_classes=(permissions.IsAuthenticated,)
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     queryset = Order.objects.all()

#     def get_queryset(self):
#         queryset = super().get_queryset().filter(user=self.request.user)
#         user = self.request.query_params.get("user")

#         if user:
#             queryset = queryset.filter(Q(user=user))

#         queryset = queryset.prefetch_related(
#             Prefetch("items", queryset=OrderItem.objects.all(), to_attr="order_items")
#         )

#         return queryset

#     def perform_create(self, serializer):
#         print(self.request.user)
#         serializer.save(user=self.request.user)

#     @action(detail=True, methods=["POST"])
#     def cancel_order(self, request, pk=None):
#         order = self.get_object()
#         if order.status == "Delivered" or order.status == "Canceled":
#             return Response(
#                 {"message": "Order cannot be canceled"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         order.status = "Canceled"
#         order.save()
#         return Response({"message": "Order cancelled successfully"})


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
    authentication_classes=(authentication.CustomUserAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)
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
