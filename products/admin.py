from django.contrib import admin
from .models import Product
from .models import ProductImage
from .models import Rating




# Register your models here.

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Rating)




