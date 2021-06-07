from django import forms

from .models import Cities

class CreateCityForm(forms.Form):
    name_of_city = forms.CharField(label='name of city', max_lenght=100, widget=froms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Cities
        fields = ('name_of_city')
