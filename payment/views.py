
import stat
import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import requests
from decouple import config
import jwt
from .models import User
from Order.models import Order, OrderItem
from user import serializer as user_serializer
from Order import serializer as order_serializer
from products.models import Product 
from products import serializers as product_serializer 
from Order.models import Order, OrderItem
from django.db import transaction
from cart.models import Cart, Cart_item
from Shipment.models import Shipment
# This is your test secret API key.
stripe.api_key = 'sk_test_51P08JABP57JOr7z5q0y7ieDJGGXoCHLDXY2nHvqrCyq5lW8F1EnTIEdUATvgRZEsV2QW1k6QQZyz4XURtqDA47HJ00iOY1WS0Q'


class StripCheckoutView(APIView):
    @transaction.atomic
    def post(self,request):
        try:
            token = request.headers.get('X-CSRFToken')
            jwt_secret = config('JWT_SECRET')
            payload = jwt.decode(token,jwt_secret,algorithms=['HS256'])

            user = User.objects.get(id=payload["id"])

            cart = Cart.objects.filter(customer_id=user.id).first()

            shipment = Shipment.objects.get(user=user)

            cart_items = Cart_item.objects.filter(cart_id=cart.id)

            order = Order.objects.create(
                total_price = 5000, #from front
                shipment_id=shipment,
                delivery_date = '2024-04-14',
                user=user
            )

            order_items = []
            for cart_item in cart_items:
                order_item = OrderItem.objects.create(
                quantity=cart_item.quantity, # from front
                price=cart_item.product_id.price,
                product=cart_item.product_id,
                order_id=order
            )
                order_items.append(order_item)

            line_items = []

            for order_item in order_items:
                price_in_cents = int(float(order_item.price) * 100)  # Convert the string price to a float first
                line_item = {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': order_item.product.name,
                            'images': [order_item.product.thumbnail.url]  # Adding the root point of the URL
                        },
                        #! all budget not more than 999,990 
                        'unit_amount': price_in_cents,  
                    },
                    'quantity': order_item.quantity,  
                }
                line_items.append(line_item)
                print(line_item)

            checkout_session = stripe.checkout.Session.create(
                    line_items=line_items,
                    mode='payment',
                    success_url='http://localhost:5173' + '?success=true&session_id={CHECKOUT_SESSION_ID}',
                    cancel_url='http://localhost:5173' + '?canceled=true',
                )
            
            cart_items.delete()

            for order_item in order_items:
                order_item.product.stock -= order_item.quantity
                order_item.product.save()

            return Response({
                'redirect_to': checkout_session.url
            })

        except stripe.error.StripeError as e:
            print(e)
            return Response({
                'error': 'Error happened'
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
