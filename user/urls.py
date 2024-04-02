from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.RegisterApi.as_view(), name="register"),
    path("login/", views.LoginApi.as_view(), name="login"),
    path("me/",views.UserApi.as_view(),name="me"), #! check this route must open when i am authorized 
    path("logout/", views.Logout.as_view(), name="logout")
]
