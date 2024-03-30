from django.conf import settings
from rest_framework import authentication, exceptions
import jwt
from . import models
import os
from dotenv import load_dotenv
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = os.path.join(BASE_DIR, 'config', '.env')
load_dotenv(dotenv_path)


class CustomUserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            return None
        
        try:
            jwt_secret = os.environ.get('JWT_SECRET')
            print(jwt_secret)
            payload = jwt.decode(token,jwt_secret,algorithms=['HS256'])
        except:
            raise exceptions.AuthenticationFailed("Unauthorized")

        user = models.User.objects.filter(id=payload["id"]).first()
        return(user,None)
    

