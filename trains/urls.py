from django.urls import path

from .views import *

urlpatterns = [
    path('', ViewTrains.as_view(), name='view_trains'),
    path('add_train/', AddTrain.as_view(), name='add_train'),
    path('train/<int:train_pk>/', ViewTrain.as_view(), name='view_train'),
    #    path('edit_city/<int:city_pk>/', EditCity.as_view(), name='edit_city'),
    #    path('delete_city/<int:city_pk>/', DeleteCity.as_view(), name='delete_city'),
]
