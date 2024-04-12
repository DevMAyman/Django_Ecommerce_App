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
