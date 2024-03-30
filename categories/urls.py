from django.urls import path 
from . import views

urlpatterns=[
    path('', views.GetCategories,name='get_categories'),
    path('<slug:slug>/', views.GetCategoryProducts, name='get_category_products'),

]