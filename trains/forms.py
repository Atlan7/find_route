from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime, timezone

from trains.models import Train
from cities.models import City


class AddTrainForm(forms.ModelForm):
    train_number = forms.IntegerField(
        label='Input train number',
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Input train number'
            }
        )
    )
    from_city = forms.ModelChoiceField(
        label='Choice start city',
        queryset=City.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )
    to_city = forms.ModelChoiceField(
        label='Choice end city',
        queryset=City.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )
    trip_start_time = forms.DateTimeField(
        label='From',
        input_formats=['%d-%m-%Y %H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control',
                'placeholder': '31-12-2021 20:20'
            }
        )
    )
    trip_end_time = forms.DateTimeField(
        label='To',
        input_formats=['%d-%m-%Y %H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control',
                'placeholder': '31-12-2021 20:20'
            }
        )
    )

    class Meta:
        model = Train
        fields = ('train_number', 'from_city', 'to_city', 'trip_start_time', 'trip_end_time',)

    def clean_trip_start_time(self):
        trip_start_time = self.cleaned_data['trip_start_time']
        if datetime.now(timezone.utc) > trip_start_time:
            raise ValidationError("Train can't departs at the past!")
        return trip_start_time
