from django.urls import path

from .views import *

urlpatterns = [
    path('', ViewCities.as_view(), name='view_cities'),
    path('add_city/', AddCity.as_view(), name='add_city'),
    path('city/<int:city_pk>/', ViewCity.as_view(), name='view_city'),
    path('edit_city/<int:city_pk>/', EditCity.as_view(), name='edit_city'),
    path('delete_city/<int:city_pk>/', DeleteCity.as_view(), name='delete_city'),
    path('trains_from_city/<int:from_city_pk>/', ViewTrainsFromCity.as_view(), name='trains_from_city'),
    path('trains_to_city/<int:to_city_pk>/', ViewTrainsToCity.as_view(), name='trains_to_city'),
]
