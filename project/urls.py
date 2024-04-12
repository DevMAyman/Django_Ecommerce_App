from django.contrib import admin
from django.urls import path, include , include
import payment.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include("user.urls")),
    path('',include('cart.urls')),
    path('',include('products.urls')),
    path('',include('categories.urls')),
    path('',include('Shipment.urls')),
    path('', include('Order.urls')),
    path('stripe/', include(payment.urls))
]


