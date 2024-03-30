import datetime

from django.core.exceptions import ValidationError
from django.db import models


class Shipment(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    shipment_creation_date = models.DateField(default=datetime.date.today)
    delivery_date = models.DateField()
    # add customer fk

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        if self.delivery_date < datetime.date.today():
            raise ValidationError("Delivery date cannot be in the past")
