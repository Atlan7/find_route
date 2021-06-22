from django.db import models

from cities.models import City
from trains.models import Train


class Route(models.Model):
    route_name = models.CharField(max_length=100, unique=True, verbose_name='Route name')
    from_city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='route_from_city_set', verbose_name='from city'
    )
    to_city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='route_to_city_set', verbose_name='to city'
    )
    trip_start_time = models.DateTimeField()
    trip_end_time = models.DateTimeField()
    trains = models.ManyToManyField(Train, verbose_name='List of trains')

    @property
    def total_trip_time(self):
        return self.trip_end_time - self.trip_start_time

    def __str__(self):
        return f'Route: {self.route_name}, '\
               f'goes from: {self.from_city} ' \
               f'to: {self.to_city}, ' \
               f'departs at: {self.trip_start_time}, ' \
               f'arrives at: {self.trip_end_time}, ' \
               f'total trip time: {self.trip_end_time - self.trip_start_time} '

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'
        ordering = ['route_name']
