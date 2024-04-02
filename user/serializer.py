from rest_framework import serializers
from . import services 

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) #! Do not make any one change id by api
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    image = serializers.ImageField()
    password = serializers.CharField(write_only=True) #!Do not return password ever in api response
    

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        return services.UserDataClass(**data)