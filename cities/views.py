from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
#from django.views.generic.edit import FormView

from .models import City
from .forms import AddCityForm


class ViewCities(ListView):
    model = City
    template_name = 'cities/cities_list.html'
    context_object_name = 'cities'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return City.objects.all()


class ViewCity(DetailView):
    model = City
    template_name = 'cities/view_city.html'
    context_object_name = 'city'
    pk_url_kwarg = 'city_pk'


class AddCity(CreateView):
    form_class = AddCityForm
    template_name = 'cities/add_city.html'
    success_url = reverse_lazy('cities:view_cities')
    raise_exception = True


class EditCity(UpdateView):
    model = City
    form_class = AddCityForm
    template_name = 'cities/edit_city.html'
    pk_url_kwarg = 'city_pk'
    success_url = reverse_lazy('cities:view_cities')
    raise_exception = True
