from rest_framework import serializers
from .models import Shipment


def validate_data_existence(data, field_name):
    if not data.get(field_name):
        raise serializers.ValidationError(f"The {field_name.replace('_', ' ')} cannot be empty")


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = "__all__"

    def validate(self, data):
        fields_to_validate = [
            "address",
            "city",
            "state",
            "country",
            "zip_code",
            "shipment_creation_date",
        ]

        for field in fields_to_validate:
            validate_data_existence(data, field)

        return data
