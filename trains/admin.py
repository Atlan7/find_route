from django.contrib import admin

from trains.models import Train


class TrainAdmin(admin.ModelAdmin):
    class Meta:
        model = Train
    list_display = ('train_number', 'from_city', 'to_city', 'trip_start_time', 'trip_end_time',)


admin.site.register(Train, TrainAdmin)


