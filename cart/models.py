from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from user.models import User
from products.models import Product

# Create your models here.
class Cart(models.Model):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')

class Cart_item(models.Model):
    quantity = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    cart_id = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart_items')

class Wishlist(models.Model):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlists')
    cart_id = models.IntegerField(default = 0)

@receiver(pre_delete, sender=Wishlist)
def remove_cart_items_on_wishlist_delete(sender, instance, **kwargs):
    # Delete related cart items when a Wishlist is deleted
    Cart_item.objects.filter(cart_id=instance.cart_id).delete()
