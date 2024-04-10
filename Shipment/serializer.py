from rest_framework import serializers
from .models import Shipment

def validate_data_existence(data, field_name):
    if not data.get(field_name):
        raise serializers.ValidationError(f"The {field_name.replace('_', ' ')} cannot be empty")

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = "__all__"
        
    def to_representation(self, instance):
        # Exclude 'user' field from the representation
        representation = super().to_representation(instance)
        representation.pop('user', None)
        return representation

    def validate(self, data):
        fields_to_validate = [
            "address",
            "city",
            "state",
            "country",
            "zip_code",
            "phone",
        ]

        for field in fields_to_validate:
            validate_data_existence(data, field)

        # Custom validation to check if the shipment already exists in the database
        address = data.get("address")
        city = data.get("city")
        state = data.get("state")
        country = data.get("country")
        zip_code = data.get("zip_code")
        phone = data.get("phone")

        existing_shipments = Shipment.objects.filter(
            address=address,
            city=city,
            state=state,
            country=country,
            zip_code=zip_code,
            phone=phone,
        )

        if self.instance:  # Exclude current instance if updating
            existing_shipments = existing_shipments.exclude(pk=self.instance.pk)

        if existing_shipments.exists():
            raise serializers.ValidationError("This shipment already exists")

        return data
