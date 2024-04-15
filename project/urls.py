from django.contrib import admin
from django.urls import path, include , include
import payment.urls
from django.conf.urls.static import static
from django.conf import settings

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

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)


