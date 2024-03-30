from django.contrib import admin
from cart.models import Cart , Cart_item , Wishlist
# Register your models here.
admin.site.register(Cart)
admin.site.register(Cart_item)
admin.site.register(Wishlist)
