from django.urls  import  path
from .views import StripCheckoutView

urlpatterns = [
    path('create-checkout-session',StripCheckoutView.as_view())
]