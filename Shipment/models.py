import datetime

from django.core.exceptions import ValidationError
from django.db import models


class Shipment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]
    
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    shipment_creation_date = models.DateField(default=datetime.date.today)
    delivery_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    # add customer fk

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        if self.delivery_date < datetime.date.today():
            raise ValidationError("Delivery date cannot be in the past")
    
    class Meta:
        verbose_name = "Shipment"
        verbose_name_plural = "Shipments"
        
    def __str__(self):
        return f"{self.id}"
