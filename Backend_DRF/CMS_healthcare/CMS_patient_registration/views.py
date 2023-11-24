from rest_framework import viewsets
from . serializers import PersonalSerializer, AddressDetailsSerializer, ContactDetailsSerializer
# from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Personal, AddressDetails, ContactDetails


class PersonalViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalSerializer
    queryset = Personal.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly]

class AddressDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = AddressDetailsSerializer
    queryset = AddressDetails.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly]

class ContactDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = ContactDetailsSerializer
    queryset = ContactDetails.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly]



