import re
from django.shortcuts import render
from requests import delete
from cart.models import Cart,Cart_item,Wishlist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status , viewsets, permissions, views
from cart.serializers import CartSerializer,CartItemsSerializer,WishListSerializer
from user import  authentication
from decouple import config
import jwt
from user.models import User 
from django.db import transaction

# Create your views here.
class Viewset_Cart(viewsets.ModelViewSet):
    # authentication_classes=(authentication.CustomUserAuthentication,)
    # permission_classes=(permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class Viewset_CartItems(viewsets.ModelViewSet):
    # authentication_classes=(authentication.CustomUserAuthentication,)
    # permission_classes=(permissions.IsAuthenticated,)
    queryset = Cart_item.objects.all()
    serializer_class = CartItemsSerializer

class Viewset_Wishlist(viewsets.ModelViewSet):
    # authentication_classes=(authentication.CustomUserAuthentication,)
    # permission_classes=(permissions.IsAuthenticated,)
    queryset = Wishlist.objects.all()
    serializer_class = WishListSerializer


# find the specific cart items depend on cartId
class searchCartItems(views.APIView):
    # authentication_classes = [authentication.CustomUserAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request, cardId):
        cart_items = Cart_item.objects.filter(cart_id=cardId)
        serializer = CartItemsSerializer(cart_items, many=True)
        return Response(serializer.data)


# find the cart depend on customerId
class searchCustomerCart(views.APIView):
    # authentication_classes = [authentication.CustomUserAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request, customerId):
        customer_cart = Cart.objects.filter(customer_id=customerId)
        serializer = CartSerializer(customer_cart, many=True)
        return Response(serializer.data)

# find the wish lists depend on customerId
class searchCustomerWishlists(views.APIView):
    # authentication_classes = [authentication.CustomUserAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request, customerId):
        customer_wishlists = Wishlist.objects.filter(customer_id=customerId)
        serializer = WishListSerializer(customer_wishlists, many=True)
        return Response(serializer.data)
    
class CartProduct(views.APIView):
    @transaction.atomic
    def post(self, request):
        try:
            token = request.headers.get('X-CSRFToken')
            jwt_secret = config('JWT_SECRET')
            payload = jwt.decode(token, jwt_secret, algorithms=['HS256'])
            user = User.objects.get(id=payload["id"])

            cart = Cart.objects.filter(customer_id=user.id).first()
            if not cart:
                return Response({"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)

            cart_items = Cart_item.objects.filter(cart_id=cart.id)
            if not cart_items:
                return Response({"error": "Cart items not found."}, status=status.HTTP_404_NOT_FOUND)

            for cart_item in cart_items:
                cart_item.product_id.stock -= cart_item.quantity
                if cart_item.product_id.stock < 0:
                    cart_item.product_id.stock = 0
                cart_item.product_id.save()

            cart_items.delete()
            return Response({"message": "Cart products processed successfully."}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



            


            cart_items = Cart_item.objects.filter(cart_id=cart.id)
            for cart_item in cart_items:
                print(cart_item)

    







