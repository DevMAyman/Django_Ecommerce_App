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
    path('cartitem/searchitems/<int:cardId>/', views.searchCartItems),
    path('cart/searchcustomercart/<int:customerId>/', views.searchCustomerCart),
    path('cart/searchcustomerwishlists/<int:customerId>/', views.searchCustomerWishlists),
    path('',include(router.urls)),
]
