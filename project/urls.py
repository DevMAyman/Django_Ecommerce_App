from django.contrib import admin
from django.urls import path , include
from cart import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from user.authentication import CustomUserAuthentication
from rest_framework.permissions import IsAuthenticated





router = DefaultRouter()
router.register('cart',views.Viewset_Cart)
router.register('cartitem',views.Viewset_CartItems)
router.register('wishlist',views.Viewset_Wishlist)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include("user.urls")),
    path('cartitem/searchitems/<int:cardId>/', views.searchCartItems.as_view()),
    path('cart/searchcustomercart/<int:customerId>/', views.searchCustomerCart.as_view()),
    path('cart/searchcustomerwishlists/<int:customerId>/', views.searchCustomerWishlists.as_view()),
    path('',include(router.urls)),
]


