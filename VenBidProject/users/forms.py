from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required.')
    confirmemail = forms.EmailField(max_length=254, help_text='Enter same email as before for verification.')
    companyname = forms.CharField(max_length=40, required=True)
    mobileno = forms.CharField(max_length=15, required=True)
    telephone = forms.CharField(max_length=15, required=True)
    addresslane1 = forms.CharField(max_length=100, required=True)
    addresslane2 = forms.CharField(max_length=100, required=True)
    city = forms.CharField(max_length=50, required=True)
    postalzip = forms.CharField(max_length=15, required=True)
    country = forms.CharField(max_length=50, required=True)
    state = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'confirmemail', 'password1', 'password2', 'companyname', 'mobileno', 'telephone', 'addresslane1', 'addresslane2', 'city', 'postalzip', 'country', 'state')