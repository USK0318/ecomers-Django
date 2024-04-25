from django.forms import ModelForm  
from django import forms
from .models import Product, user_info
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class productform(forms.ModelForm):
    class Meta:
        model=Product
        fields=['product_name','price','desc','image']

class registerform(UserCreationForm):
    class Meta:
        model=User
        fields= ['username','email','password1','password2','first_name','last_name']

class editform(forms.ModelForm):
    class Meta:
        model=user_info
        fields='__all__'