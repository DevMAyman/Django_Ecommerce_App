from .serializer import ShipmentSerializer
from .models import Shipment
from rest_framework import viewsets, permissions
from user import  authentication
  
class ShipmentViewSet(viewsets.ModelViewSet):
  authentication_classes=(authentication.CustomUserAuthentication,)
  permission_classes=(permissions.IsAuthenticated,)
  queryset = Shipment.objects.all()
  serializer_class = ShipmentSerializer
