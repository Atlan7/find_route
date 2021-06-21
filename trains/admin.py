from django.contrib import admin

from trains.models import Train


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('train_number', 'from_city', 'to_city', 'trip_start_time', 'trip_end_time', 'total_trip_time',)



