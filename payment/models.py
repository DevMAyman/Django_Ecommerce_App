from django.db import models
from user.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Payment(models.Model):
    user_payment = models.ForeignKey(User,on_delete=models.CASCADE)
    payment_bool = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=500)


#!create payment every time user created 
# @receiver(post_save, sender=User)
# def create_user_payment(sender, instance, created, **kwargs):
#     if created:
#         Payment.objects.create(User=instance)
    

