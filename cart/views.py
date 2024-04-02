from django.shortcuts import render
from cart.models import Cart,Cart_item,Wishlist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status , viewsets, permissions, views
from cart.serializers import CartSerializer,CartItemsSerializer,WishListSerializer
from user import  authentication
# Create your views here.
class Viewset_Cart(viewsets.ModelViewSet):
    authentication_classes=(authentication.CustomUserAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class Viewset_CartItems(viewsets.ModelViewSet):
    authentication_classes=(authentication.CustomUserAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)
    queryset = Cart_item.objects.all()
    serializer_class = CartItemsSerializer

class Viewset_Wishlist(viewsets.ModelViewSet):
    authentication_classes=(authentication.CustomUserAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)
    queryset = Wishlist.objects.all()
    serializer_class = WishListSerializer


# find the specific cart items depend on cartId
class searchCartItems(views.APIView):
    authentication_classes = [authentication.CustomUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, cardId):
        cart_items = Cart_item.objects.filter(cart_id=cardId)
        serializer = CartItemsSerializer(cart_items, many=True)
        return Response(serializer.data)


# find the cart depend on customerId
class searchCustomerCart(views.APIView):
    authentication_classes = [authentication.CustomUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, customerId):
        customer_cart = Cart.objects.filter(customer_id=customerId)
        serializer = CartSerializer(customer_cart, many=True)
        return Response(serializer.data)

# find the wish lists depend on customerId
class searchCustomerWishlists(views.APIView):
    authentication_classes = [authentication.CustomUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, customerId):
        customer_wishlists = Wishlist.objects.filter(customer_id=customerId)
        serializer = WishListSerializer(customer_wishlists, many=True)
        return Response(serializer.data)




