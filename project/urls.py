from django.contrib import admin
from django.urls import path , include
from cart import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cart',views.Viewset_Cart)
router.register('cartitem',views.Viewset_CartItems)
router.register('wishlist',views.Viewset_Wishlist)

urlpatterns = [
    path('admin/', admin.site.urls),
]
