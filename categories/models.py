from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'categories'
