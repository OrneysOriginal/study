from django import forms
from django.forms import ModelForm
from app_advertisements.models import Advertisements


class AdvertisementsForm(ModelForm):
    class Meta:
        model = Advertisements
        fields = ['title','description','price','auction']
