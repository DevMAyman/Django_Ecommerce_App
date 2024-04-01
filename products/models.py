from django.db import models
from django.utils import timezone
from categories.models import Category
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    thumbnail = models.ImageField(upload_to='photos/products/%y/%m/%d')
    rating = models.IntegerField(default=0)  
    stock = models.IntegerField(default=0)
    created_at=models.DateTimeField(default=timezone.now)
    def __str__(self) :
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/products/%y/%m/%d')
    def __str__(self):
        return f"Image for {self.product.name}"   


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,limit_choices_to={'is_superuser': 0})
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='ratings')
    user_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    class Meta:
        unique_together = ('user', 'product')  

    def __str__(self):
        return f"{self.user.username} rated {self.product.name} {self.user_rating} stars"

@receiver(post_save, sender=Rating)
def update_product_rating(sender, instance, **kwargs):
    product = instance.product
    ratings = Rating.objects.filter(product=product)
    average_rating = ratings.aggregate(models.Avg('user_rating'))['user_rating__avg'] or 0
    product.rating = round(average_rating, 2)
    product.save()