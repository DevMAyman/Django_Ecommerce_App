
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
# This is your test secret API key.
stripe.api_key = 'sk_test_51P08JABP57JOr7z5q0y7ieDJGGXoCHLDXY2nHvqrCyq5lW8F1EnTIEdUATvgRZEsV2QW1k6QQZyz4XURtqDA47HJ00iOY1WS0Q'


class StripCheckoutView(APIView):
    def post(self,request):
        token = request.headers.get('X-CSRFToken')
        jwt_secret = config('JWT_SECRET')
        payload = jwt.decode(token,jwt_secret,algorithms=['HS256'])

        #! get user for specific id which is sent i jwt 
        user = User.objects.get(id=payload["id"])

        order = Order.objects.filter(user=user).order_by('-order_creation_date').first()
        my_order= order_serializer.OrderSerializer(order,many=True)
        order_items_with_products = OrderItem.objects.filter(order_id=order.id).select_related('product_id')

        order_item_serializer = order_serializer.OrderItemSerializer(order_items_with_products, many=True)
        line_items = []

        for order_item in order_item_serializer.data:
            price_in_cents = int(float(order_item['price']) * 100)  # Convert the string price to a float first
            line_item = {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': order_item['product_id']['name'],
                        'images': ['http://res.cloudinary.com/dct8gxufm/' + order_item['product_id']['thumbnail']]  
                    },
                    #! all budget not more than 999,990 
                    'unit_amount': 500,  
                },
                'quantity': order_item['quantity'],  
            }
            line_items.append(line_item)
            print(line_item)
        try:
                checkout_session = stripe.checkout.Session.create(
                    line_items=line_items,
                    mode='payment',
                    success_url='http://localhost:5177' + '?success=true&session_id={CHECKOUT_SESSION_ID}',
                    cancel_url='http://localhost:5177' + '?canceled=true',
                )

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

# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
import stripe

@receiver(post_save, sender=Product)
def create_stripe_product(sender, instance, created, **kwargs):
    if created:
        stripe.api_key = "sk_test_51P08JABP57JOr7z5q0y7ieDJGGXoCHLDXY2nHvqrCyq5lW8F1EnTIEdUATvgRZEsV2QW1k6QQZyz4XURtqDA47HJ00iOY1WS0Q"
        try:
            stripe_product= stripe.Product.create(name=instance.name)
            print(stripe_product)
            # instance.stripe_name = stripe_product.name
            instance.save()

        except stripe.error.StripeError as e:
            print("Failed to create product in Stripe:", e)
