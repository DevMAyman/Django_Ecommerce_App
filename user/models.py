from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField

class UserManager(BaseUserManager):
    
    def create_user(self, first_name: str, last_name: str, email: str, phone: str, image: str = None, password: str = None, is_staff=False, is_superuser=False) -> "User":
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have last name")
        if not phone:
            raise ValueError("User must have a phone number")

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.phone = phone
        user.set_password(password)
        user.image = image
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user
    
    def create_superuser(self, first_name: str, last_name: str, email: str, phone: str, password: str) -> "User":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        return user

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=255)
    image = CloudinaryField('image')
    phone = models.CharField(max_length=20, unique=True)
    username=None
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone"]

    def clean(self):
        # Call the clean method of the parent class
        super().clean()

        # Check for uniqueness of phone number
        if User.objects.filter(phone=self.phone).exclude(pk=self.pk).exists():
            raise ValidationError({'phone': 'This phone number is already in use.'})
        if User.objects.filter(phone=self.phone).exclude(pk=self.pk).exists():
            raise ValidationError({'phone': 'This phone number is already in use.'})


