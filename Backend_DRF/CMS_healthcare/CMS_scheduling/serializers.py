import re
from rest_framework import serializers
from .models import ServiceProvider, RoomCategory
from rest_framework.serializers import ValidationError
# from django.core.validators import RegexValidator
# from django.core import validators


def NameValidator(value):
    regex = r'^[A-Z][a-z]*$'
    message = "Name must only contain letters and start with an uppercase letter"
    if not re.match(regex, value):
        raise ValidationError(message)

def pcode(value):
    regex = r'^[A-Z][a-z][0-9]*$'
    message = "Name must only contain letters and nos"
    if not re.match(regex, value):
        raise ValidationError(message)
    

class ServiceProviderSerializer(serializers.ModelSerializer):
    service_provider_id = serializers.IntegerField()
    service_provider_name = serializers.CharField(max_length=100, validators=[NameValidator])
    service_provider_code = serializers.CharField(max_length=20, validators=[pcode])

    class Meta:
        model = ServiceProvider
        fields = "__all__"


class RoomCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomCategory
        fields = "__all__"