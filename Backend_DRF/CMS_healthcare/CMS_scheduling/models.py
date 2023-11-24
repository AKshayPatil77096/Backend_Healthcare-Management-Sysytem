from django.db import models
# from CMS_Patient_Registration.models import AddressDetails
# from CMS_Billing.models import BankDetails

room=(('AC','AC'),('Non-AC','Non-AC'),('General','General'))

class ServiceProvider(models.Model):
    service_provider_id = models.IntegerField(primary_key=True)
    service_provider_name = models.CharField(max_length=100)
    service_provider_code = models.CharField(max_length=20)
    hospital_identifier = models.BigIntegerField(default='1236547') #given by gov.
    hospital_type = models.CharField(max_length=100, default='MultiSpeciality',)
    hospital_registration_number = models.BigIntegerField(default='568932',) #given by gov.
    # address_details = models.OneToOneField(AddressDetails, on_delete=models.CASCADE)
    # bank_details = models.OneToOneField(BankDetails, on_delete=models.CASCADE)

class RoomCategory(models.Model):
    room_category_id = models.IntegerField(primary_key=True)
    room_category_name = models.CharField(max_length=50, choices=room)
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)


		