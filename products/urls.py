from django.urls import path 
from . import views

urlpatterns=[
    path('', views.GetProducts),
    path('<int:id>', views.FBV_pk),


]