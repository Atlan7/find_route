from datetime import datetime, timedelta

from django import template

from trains.models import Train

register = template.Library()


@register.filter
def has_trains_from_city(city) -> bool:
    return Train.objects.filter(
                    from_city_id=city.id,
                    trip_start_time__range=[datetime.now(), datetime.now() + timedelta(days=30)],
                    trip_end_time__range=[datetime.now(), datetime.now() + timedelta(days=30)]
                ).exists()


@register.filter
def has_trains_to_city(city) -> bool:
    return Train.objects.filter(
                    to_city_id=city.id,
                    trip_start_time__range=[datetime.now(), datetime.now() + timedelta(days=30)],
                    trip_end_time__range=[datetime.now(), datetime.now() + timedelta(days=30)]
                ).exists()
