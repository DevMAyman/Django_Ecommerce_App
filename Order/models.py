import datetime
from django.db import models
from Shipment.models import Shipment

class Order(models.Model):
  order_creation_date = models.DateField(default=datetime.date.today)
  total_price = models.DecimalField(max_digits = 10, decimal_places = 2)
  shipment_id = models.OneToOneField(Shipment, on_delete=models.CASCADE)
  # add the customer fk
  # add the payment fk
  
  
class OrderItem(models.Model):
  quantity = models.IntegerField()
  price = models.DecimalField(max_digits = 10, decimal_places = 2)
  order_id = models.ForeignKey(Order, related_name='items',on_delete=models.CASCADE)
  # add product fk
  
