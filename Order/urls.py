from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('orders',views.OrderView)
router.register('orderitem', views.OrderItemView)

urlpatterns = [
    path('', include(router.urls))
]
