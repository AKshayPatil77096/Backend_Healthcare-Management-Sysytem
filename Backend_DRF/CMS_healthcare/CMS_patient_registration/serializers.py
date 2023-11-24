import re
from rest_framework import serializers
from .models import AddressDetails,ContactDetails,Personal
from rest_framework.serializers import ValidationError
from django.core.validators import RegexValidator
from django.core import validators
from django.forms.widgets import NumberInput


def pincodenos(value):
    if len(value)!=6 or value.isalpha == True:
        raise validators.ValidationError('Enter valid Pin-Code. It should be 6 digit number')

def mobnos(value):
    if len(value)!=10 or value.isalpha == True:
        raise validators.ValidationError('Enter valid Mobile No')
def adhar(value):
    if len(value)!=12 or value.isalpha == True:
        raise validators.ValidationError('Enter valid Adhar No')
    
def NameValidator(value):
    regex = r'^[A-Z][a-z]*$'
    message = "Name must only contain letters and start with an uppercase letter"
    if not re.match(regex, value):
        raise ValidationError(message)
    

## =====================   other way ===========================================
# class NameValidator:
#     def __init__(self):
#         self.regex = r'^[A-Z][a-z]*$'
#         self.message = "Name must only contain letters and start with an uppercase letter"
    
#     def __call__(self, value):
#         if not re.match(self.regex, value):
#             raise ValidationError(self.message)



# class PasswordValidator():
#     def __init__(self):
#         self.regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
#         self.message = 'Password must contain at least one uppercase, one lowercase, one digit, one special character and must be at least 8 characters long'

#     def __call__(self, value):
#         if not re.match(self.regex, value):
#             raise ValidationError(self.message)


#=============================  other way ====================================    
#      
# class PasswordValidator(RegexValidator):
#      regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
#      message = 'Password must contain at least one uppercase, one lowercase, one digit, one special character and must be at least 8 characters long'


# Main Serializer class
class AddressDetailsSerializer(serializers.ModelSerializer):
    town = serializers.CharField(max_length=100, validators=[NameValidator])
    city = serializers.CharField(max_length=100, validators=[NameValidator])
    state = serializers.CharField(max_length=100, validators=[NameValidator])
    pincode = serializers.CharField(max_length=100,validators=[pincodenos])

    class Meta:
        model = AddressDetails
        fields = "__all__"


class ContactDetailsSerializer(serializers.ModelSerializer):
    mobile_number = serializers.CharField(max_length=100,validators=[mobnos])
    alternate_mobile_number = serializers.CharField(max_length=100,validators=[mobnos])
    email_identifier = serializers.EmailField(validators=[RegexValidator(regex='^[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.com|\.co\.in)$', message='Email does not accept domains other than "com" and "co.in" ' )])
    alternate_email_identifier = serializers.EmailField(validators=[RegexValidator(regex='^[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.com|\.co\.in)$', message='Email does not accept domains other than "com" and "co.in" ' )])
    
    class Meta:
        model = ContactDetails
        fields = "__all__"

class PersonalSerializer(serializers.ModelSerializer):
    res_first_name = serializers.CharField(max_length=80, validators=[NameValidator])
    res_last_name = serializers.CharField(max_length=50, validators=[NameValidator])
    res_middle_name = serializers.CharField(max_length=50, validators=[NameValidator])
    res_age = serializers.IntegerField(validators=[validators.MaxValueValidator(115)])
    res_weight = serializers.IntegerField(  help_text='weight should be in kg', validators=[validators.MaxValueValidator(300)])
    res_height = serializers.IntegerField( help_text='height should be in cms', validators=[validators.MaxValueValidator(200)])
    res_date_of_birth = serializers.DateTimeField(format="%d/%m/%Y")
    # res_date_of_birth= serializers.DateField(widgets=serializers.DateInput(attrs={'class':'form-control','type':'date'}))
    res_aadhar_card_number = serializers.CharField(max_length=100, validators=[adhar])
   
    class Meta:
        model = Personal
        exclude = ['res_code']
        


    # =================================    for direct field validations ========================================
    # first_name = serializers.CharField(validators=[RegexValidator(regex=r'^[A-Z][a-z]*$',
                                                                #    message='First letter of first Name must start with capital and must not contain any digit')])
    # last_name = serializers.CharField(validators=[RegexValidator(r'^[A-Z][a-z]*$',
                                                                #   message='First letter of last Name must start with capital and must not contain any digit')])
    # password = serializers.CharField(
    #     validators=[RegexValidator(regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
                                #    message='Password must contain at least one uppercase, one lowercase, one digit, one special character and must be at least 8 characters long')])


        # if len(password) != 8:
        #     raise ValidationError('Password length must of 8 chars')
       
        # if not data['first_name'].isalpha() or not data['last_name'].isalpha():
        #     raise ValidationError('Name must not contain any digit')
       
        # if not data['first_name'][0].isupper() or not data['last_name'][0].isupper():
        #     raise ValidationError('First letter of Name must start with capital letter')