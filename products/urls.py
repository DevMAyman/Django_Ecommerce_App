from django.urls import path,include 
from . import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('',views.Viewset_Products)
router.register('product/images',views.Viewset_ProductImages)


urlpatterns=[
    path('',include(router.urls)),

]