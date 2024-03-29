from django.shortcuts import render
from cart.models import Cart,Cart_item,Wishlist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status , viewsets
from cart.serializers import CartSerializer,CartItemsSerializer,WishListSerializer

# Create your views here.
class Viewset_Cart(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class Viewset_CartItems(viewsets.ModelViewSet):
    queryset = Cart_item.objects.all()
    serializer_class = CartItemsSerializer

class Viewset_Wishlist(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishListSerializer


# find the specific cart items depend on cartId
@api_view(['GET'])
def searchCartItems(request , cardId):
    Cart_items = Cart_item.objects.filter(cart_id= cardId)
    serializer = CartItemsSerializer(Cart_items , many = True)
    return Response(serializer.data)

# find the cart depend on customerId
@api_view(['GET'])
def searchCustomerCart(request , customerId):
    CustomerCart = Cart.objects.filter(customer_id= customerId)
    serializer = CartSerializer(CustomerCart , many = True)
    return Response(serializer.data)

# find the wish lists depend on customerId
@api_view(['GET'])
def searchCustomerWishlists(request , customerId):
    CustomerWishlists = Wishlist.objects.filter(customer_id= customerId)
    serializer = WishListSerializer(CustomerWishlists , many = True)
    return Response(serializer.data)




