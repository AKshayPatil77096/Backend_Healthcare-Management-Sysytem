from django.db import models
# from django.core import validators

# Create your models here.
m=(('married','married'), ('unmarried','unmarried'))
g=(('male','male'), ('female','female'),('other','other'))
h=(('No','No'),('Yes','Yes'))
claim=(('No','No'),('Yes','Yes'))
prefix=(('Mrs','Mrs'),('Mr','Mr'),('Ms','Ms'))


class AddressDetails(models.Model):
    address_details_id = models.IntegerField()
    line1 = models.CharField(max_length=200)
    line2 = models.CharField(max_length=200)
    landmark = models.CharField(max_length=100, blank=True)
    area = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()

    class Meta:
        managed = False

class ContactDetails(models.Model):
    contact_details_id = models.IntegerField(primary_key=True)
    mobile_number = models.BigIntegerField()
    alternate_mobile_number = models.BigIntegerField()
    email_identifier = models.EmailField()
    alternate_email_identifier = models.EmailField()

    class Meta:
        managed = False

class Personal(models.Model):
    personal_id = models.IntegerField()
    res_code = models.AutoField(primary_key=True, auto_created = True)
    claim_status = models.CharField(max_length=50, choices=claim)
    res_first_name = models.CharField(max_length=80)
    res_last_name = models.CharField(max_length=50)
    res_middle_name = models.CharField(max_length=50, blank=True)
    res_name_prefix = models.CharField(max_length=50, blank=True, choices=prefix)
    res_name_suffix = models.CharField(max_length=10, blank=True)
    res_age = models.PositiveIntegerField()
    res_weight = models.PositiveIntegerField()
    res_height = models.PositiveIntegerField()
    res_image = models.ImageField(upload_to='personal_images/', blank=True,)
    res_marital_status = models.CharField(max_length=10, choices=m)
    res_gender = models.CharField(max_length=10, choices=g)
    res_is_handicap =  models.CharField(max_length=50, choices=h)
    res_date_of_birth = models.DateField()
    res_occupation = models.CharField(max_length=50, blank=True)
    res_aadhar_card_number = models.BigIntegerField( blank=True)
    res_aadhar_card_image = models.ImageField(upload_to='aadhar_card_images/', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    address_details = models.OneToOneField(AddressDetails, on_delete=models.CASCADE)
    contact_details = models.OneToOneField(ContactDetails, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.res_first_name} {self.res_last_name}"

    class Meta:
        managed = False

