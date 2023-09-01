from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from app_advertisements.models import Advertisements


class AdvertisementsForm(ModelForm):
    class Meta:
        model = Advertisements
        fields = ['title','description','price','auction']


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(min_length=6, max_length=35)
    name = forms.CharField(min_length=3, max_length=30)
    surname = forms.CharField(min_length=3, max_length=35)
    password1 = forms.CharField(min_length=6,max_length=20, widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=6, max_length=20, widget=forms.PasswordInput)