from django.contrib import admin

from trains.models import Train


class TrainAdmin(admin.ModelAdmin):
    class Meta:
        model = Train



admin.site.register(Train)


