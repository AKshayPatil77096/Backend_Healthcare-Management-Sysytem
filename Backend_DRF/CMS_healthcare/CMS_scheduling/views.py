from rest_framework import viewsets
from . serializers import ServiceProviderSerializer, RoomCategorySerializer
# from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly, IsAdminUser
from .models import ServiceProvider, RoomCategory


class ServiceProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceProviderSerializer
    queryset = ServiceProvider.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly]

class RoomCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = RoomCategorySerializer
    queryset = RoomCategory.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly]
