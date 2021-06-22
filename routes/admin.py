from django.contrib import admin

from .models import Route


@admin.register(Route)
class AdminRoute(admin.ModelAdmin):
    list_display = (
        'route_name',
        'from_city',
        'to_city',
        'trip_start_time',
        'trip_end_time',
        'total_trip_time',
    )



