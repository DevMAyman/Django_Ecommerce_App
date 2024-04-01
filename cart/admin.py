from django.contrib import admin
from cart.models import Cart , Cart_item , Wishlist
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False  # Disallow adding instances
    
    def has_delete_permission(self, request, obj=None):
        return False  # Disallow deleting instances
    
    def has_change_permission(self, request, obj=None):
        return False  # Disallow deleting instances


class Cart_itemAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False  # Disallow adding instances
    
    def has_delete_permission(self, request, obj=None):
        return False  # Disallow deleting instances
    
    def has_change_permission(self, request, obj=None):
        return False  # Disallow deleting instances


class WishlistAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False  # Disallow adding instances
    
    def has_delete_permission(self, request, obj=None):
        return False  # Disallow deleting instances
    
    def has_change_permission(self, request, obj=None):
        return False  # Disallow deleting instances


admin.site.register(Cart,CartAdmin)
admin.site.register(Cart_item,Cart_itemAdmin)
admin.site.register(Wishlist,WishlistAdmin)
