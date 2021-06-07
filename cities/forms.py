from django import forms

from .models import City


# class AddCityForm(forms.Form):
#     name = forms.CharField(label='City')

class AddCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={
        	'class': 'form-control',
        	'placeholder': 'Put name of the city'
        	})}
