from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'image', 'password', 'phone']
        extra_kwargs = {
            'password': {'write_only': True},  # Do not include 'password' field in response
            'id': {'read_only': True},         # Do not allow 'id' to be updated via API
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Construct the full image URL using Cloudinary transformation
        if representation.get('image'):
            representation['image'] = instance.image.build_url(transformation=[
                {'width': 200, 'height': 200, 'crop': 'thumb', 'gravity': 'face'},  # Example transformation
            ])
        return representation

    def update(self, instance, validated_data):
        # Override update method to handle image update
        return super().update(instance, validated_data)
