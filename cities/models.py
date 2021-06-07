from django.db import models
from django.urls import reverse_lazy


# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse_lazy('cities:view_city', kwargs={'city_pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['name']
