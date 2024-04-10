import datetime
from django.db import models
from Shipment.models import Shipment
from user.models import User 
from products.models import Product
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled')
    ]
     
    order_creation_date = models.DateTimeField(default=datetime.date.today)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipment_id = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    user = models.ForeignKey(User, on_delete=models.CASCADE,limit_choices_to={'is_superuser': 0})


    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        
    def __str__(self):
        return f"{self.id}"


class OrderItem(models.Model):
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_id = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    # add product fk
    class Meta:
        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItem"
        
    def __str__(self):
        return f"{self.id}"
    
    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        super().save(*args, **kwargs)


