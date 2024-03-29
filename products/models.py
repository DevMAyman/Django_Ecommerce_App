from django.db import models
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self) :
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #the on_delete
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    thumbnail = models.ImageField(upload_to='photos/products/%y/%m/%d')
    #images
    #rating
    stock = models.IntegerField(default=0)
    created_at=models.DateTimeField(default=timezone.now)
    def __str__(self) :
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/products/%y/%m/%d')


