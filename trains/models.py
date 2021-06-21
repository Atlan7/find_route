from django.db import models
from django.core.exceptions import ValidationError

from cities.models import City


class Train(models.Model):
    train_number = models.PositiveIntegerField(unique=True, verbose_name='train number')
    from_city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='from_city_set', verbose_name='from city'
    )
    to_city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='to_city_set', verbose_name='to city'
    )
    trip_start_time = models.DateTimeField()
    trip_end_time = models.DateTimeField()

    @property
    def total_trip_time(self):
        return self.trip_end_time - self.trip_start_time

    def clean(self):
        try:
            if self.trip_start_time > self.trip_end_time:
                raise ValidationError("Start time of trip can't exceed end time of trip !")
            elif self.from_city == self.to_city:
                raise ValidationError("Start point of departs can't be equal end point !")
        except TypeError as e:
            pass

    def __str__(self):
        return f'Train number: №{self.train_number}, ' \
               f'goes from: {self.from_city} ' \
               f'to: {self.to_city}, ' \
               f'departs at: {self.trip_start_time}, ' \
               f'arrives at: {self.trip_end_time}, ' \
               f'total trip time: {self.trip_end_time - self.trip_start_time} '

    class Meta:
        verbose_name = 'Train'
        verbose_name_plural = 'Trains'
        ordering = ['train_number']
