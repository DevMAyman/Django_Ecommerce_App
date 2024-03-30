from django.urls import path,include 
from . import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
# router.register('',views.Viewset_categories)

urlpatterns=[
    path('categories/',views.GetAllCategories),
    path('',include(router.urls)),
]