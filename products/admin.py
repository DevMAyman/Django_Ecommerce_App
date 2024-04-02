from django.contrib import admin
from .models import Product
from .models import ProductImage
from .models import Rating




class RatingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False  # Disallow adding instances
    
    def has_delete_permission(self, request, obj=None):
        return False  # Disallow deleting instances
    
    def has_change_permission(self, request, obj=None):
        return False  # Disallow deleting instances


# Register your models here.

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Rating, RatingAdmin)




