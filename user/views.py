from uu import decode
import jwt
from rest_framework import views, response, exceptions, permissions
from . import serializer as user_serializer
from . import services, authentication
from rest_framework import status
from decouple import config
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError
from .models import User
class RegisterApi(views.APIView):
    def post(self, request):
        try:
            serializer = user_serializer.UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            validated_data = serializer.validated_data  # Get validated data from serializer
            user_instance = services.UserDataClass(**validated_data)  # Create instance of UserDataClass from validated data
            serializer.instance = services.create_user(user_dc=user_instance)
            return response.Response(data=serializer.data)
        except IntegrityError as e:
            if 'Duplicate entry' in str(e) and 'email' in str(e):
                return response.Response({'error': 'This email is already in use.'}, status=409)  # Custom message and status code for duplicate email
            elif 'Duplicate entry' in str(e) and 'phone' in str(e):
                return response.Response({'error': 'This phone is already in use.'}, status=409)  # Custom message and status code for duplicate email  
            else:
                return response.Response({'error': 'Internal Server Error'}, status=500)  # Return the original IntegrityError message with status code 400




class LoginApi(views.APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            raise exceptions.AuthenticationFailed("Please provide both email and password.")

        user = services.user_email_selector(email=email)
        if user is None:
            raise exceptions.AuthenticationFailed("User or password incorrect")
        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("User or password incorrect")

        # Serialize the user object
        serializer = user_serializer.UserSerializer(user)

        token = services.create_token(user_id=user.id, is_superuser=user.is_superuser)
        user_info = serializer.data  # Use the serialized data
        
        # Set the JWT token as a cookie in the response
        response_obj = response.Response({'token': token, 'user_info': user_info})
        response_obj.set_cookie(key='jwt', value=token, httponly=True)
        
        return response_obj

    
class UserApi(views.APIView):
    authentication_classes=(authentication.CustomUserAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)

    def get(self,request):
        user=request.user
        serializer = user_serializer.UserSerializer(user)
        return response.Response(serializer.data)
    def patch(self, request):
        token = request.headers.get('X-CSRFToken')
        if not token:
            return None
        
        try:
            jwt_secret = config('JWT_SECRET')
            payload = jwt.decode(token,jwt_secret,algorithms=['HS256'])
            print(payload)
        except:
            raise exceptions.AuthenticationFailed("Unauthorized")


        try:
            user = User.objects.get(id=payload["id"])
            serializer = user_serializer.UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data)
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return response.Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
       
        

class Logout(views.APIView):
    authentication_classes=(authentication.CustomUserAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)

    def post(self,request):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data={"message":"so long"}
        return resp


