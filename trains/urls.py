from django.urls import path

from .views import *

urlpatterns = [
    path('', ViewTrains.as_view(), name='view_trains'),
    path('add_train/', AddTrain.as_view(), name='add_train'),
    path('train/<int:train_pk>/', ViewTrain.as_view(), name='view_train'),
    path('edit_train/<int:train_pk>/', EditTrain.as_view(), name='edit_train'),
    path('delete_train/<int:train_pk>/', DeleteTrain.as_view(), name='delete_train'),
]
