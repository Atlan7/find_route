from django import forms

from routes.models import Route
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
    trip_start_time = forms.DateTimeField(
        label='Start time',
        input_formats=['%d-%m-%Y %H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control',
                'placeholder': '31-12-2021 20:20'
            }
        )
    )
    trip_end_time = forms.DateTimeField(
        label='End time',
        input_formats=['%d-%m-%Y %H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control',
                'placeholder': '31-12-2021 20:20'
            }
        )
    )
    through_cities = forms.ModelMultipleChoiceField(
        label='Through cities',
        queryset=City.objects.all(),
        required=False,
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control js-example-basic-multiple'
            }
        )
    )
