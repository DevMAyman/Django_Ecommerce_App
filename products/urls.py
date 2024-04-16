from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'ratings', views.Viewset_Ratings)

urlpatterns = [
    path('', include(router.urls)),
    path('products/', views.GetAllProducts),
    path('products/<int:id>/', views.getProductById),
    path('products/<int:product_id>/images/', views.GetProductsImages),
     path('products/<int:product_id>/ratings/', views.getRatingsByProduct, name='get_ratings_by_product'),
    path('users/<int:user_id>/ratings/<int:product_id>/', views.manageUserRating, name='manage_user_rating'),
]

