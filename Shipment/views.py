from .serializer import ShipmentSerializer
from .models import Shipment
from rest_framework import viewsets, permissions
from rest_framework import filters
from user import  authentication
  
class ShipmentViewSet(viewsets.ModelViewSet):
  authentication_classes=(authentication.CustomUserAuthentication,)
  permission_classes=(permissions.IsAuthenticated,)
  queryset = Shipment.objects.all()
  serializer_class = ShipmentSerializer
  filter_backends = [filters.SearchFilter]
  def get_queryset(self):
        queryset = super().get_queryset()
        filter_type = self.request.query_params.get('filter')

        if not filter_type:
          return queryset
        
        if filter_type == 'city':
            city = self.request.query_params.get('city')
            if city:
                queryset = queryset.filter(city=city)
        elif filter_type == 'state':
            state = self.request.query_params.get('state')
            if state:
                queryset = queryset.filter(state=state)
        elif filter_type == 'country':
            country = self.request.query_params.get('country')
            if country:
                queryset = queryset.filter(country=country)

        return queryset
