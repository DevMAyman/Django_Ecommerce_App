from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your models here.
class Cart(models.Model):
    # customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='carts')
    customer_id = models.IntegerField()

class Cart_item(models.Model):
    quantity = models.IntegerField()
    product_id = models.IntegerField()
    cart_id = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart_items')

class Wishlist(models.Model):
    # customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='wishlist_items')
    cart_id = models.IntegerField(default = 0)
    customer_id = models.IntegerField()

@receiver(pre_delete, sender=Wishlist)
def remove_cart_items_on_wishlist_delete(sender, instance, **kwargs):
    # Delete related cart items when a Wishlist is deleted
    Cart_item.objects.filter(cart_id=instance.cart_id).delete()
