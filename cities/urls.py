from django.urls import path

from .views import *

urlpatterns = [
    path('', ViewCities.as_view(), name='view_cities'),
    path('add_city/', AddCity.as_view(), name='add_city'),
    path('city/<int:city_pk>/', ViewCity.as_view(), name='view_city'),
    path('edit_city/<int:city_pk>/', EditCity.as_view(), name='edit_city'),
]
