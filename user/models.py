from django.db import models
from django.contrib.auth import models as auth_models

# Create your models here.
#! Help us to make user using command 
class UserManager(auth_models.BaseUserManager):

    def create_user(self, first_name: str, last_name: str, email: str,image :str = None,password: str = None, is_staff=False, is_superuser = False) -> "User":
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have last name")

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.image= image
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user
    
    def create_superuser(self, first_name: str, last_name:str, email:str ,password:str) -> "User":
        user= self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )

        user.save()
        return user


class User(auth_models.AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    username= None

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name"]