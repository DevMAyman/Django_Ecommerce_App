from dataclasses import dataclass
from typing import TYPE_CHECKING
from . import models
import datetime
import jwt
import os
from dotenv import load_dotenv
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = os.path.join(BASE_DIR, 'config', '.env')
load_dotenv(dotenv_path)

if TYPE_CHECKING:
    from .models import User

@dataclass
class UserDataClass:
    first_name: str
    last_name: str
    email: str
    password: str = None
    id: int = None

    @classmethod
    def from_instance(cls, user: "User") -> "UserDataClass":
        return cls(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            id=user.id
        )

def create_user(user_dc: "UserDataClass") -> "UserDataClass":
    instance = models.User(
        first_name=user_dc.first_name,
        last_name=user_dc.last_name,
        email=user_dc.email,
    )
    if user_dc.password is not None:
        instance.set_password(user_dc.password)

    instance.save()

    return UserDataClass.from_instance(instance)

def user_email_selector(email:str) -> "User":
    return models.User.objects.filter(email=email).first()

def create_token(user_id: int) -> str:

    payload = {
        "id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        "iat": datetime.datetime.utcnow()
    }

    jwt_secret = os.environ.get('JWT_SECRET')
    token = jwt.encode(payload, jwt_secret, algorithm='HS256')

    return token