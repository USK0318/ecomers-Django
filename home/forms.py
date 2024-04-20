from django.forms import ModelForm  
from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class productform(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class registerform(UserCreationForm):
    class Meta:
        model=User
        fields= ['username','email','password1','password2','first_name','last_name']