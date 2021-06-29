from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta

from cities.models import City


class FindRouteForm(forms.Form):
    from_city = forms.ModelChoiceField(
        label='Choice start city',
        queryset=City.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control js-example-basic-single'
            }
        )
    )
    to_city = forms.ModelChoiceField(
        label='Choice end city',
        queryset=City.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control js-example-basic-single'
            }
        )
    )
    initial_period_for_route  = forms.DateField(
        label='Choice initial period for route',
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': f'{datetime.now():%d-%m-%Y}'
            }
        )
    )
    end_route_period = forms.DateField(
        label='Choice end of the period',
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': f'{datetime.now() + timedelta(days=5):%d-%m-%Y}'
            }
        )
   )


    def clean_end_route_period(self):
        end_route_period = self.cleaned_data['end_route_period']
        initial_period_for_route = self.cleaned_data['initial_period_for_route']
        if end_route_period < initial_period_for_route:
            raise ValidationError("End route period can't be less than initial")

        return end_route_period

