from django import forms
from django.core.exceptions import ValidationError
import re

from .models import City


class AddCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Put name of the city'
           })}


    def clean_name(self):
        name = self.cleaned_data['name']
        if re.match(r'd', name):
            raise ValidationError("City can't contain numbers")
        return name



