from datetime import datetime, timedelta

from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

from .models import City
from trains.models import Train
from .forms import AddCityForm


class ViewCities(ListView):
    model = City
    template_name = 'cities/view_cities.html'
    context_object_name = 'cities'
    paginate_by = 10


class ViewCity(DetailView):
    model = City
    template_name = 'cities/view_city.html'
    context_object_name = 'city'
    pk_url_kwarg = 'city_pk'


@method_decorator(user_passes_test(lambda user: user.is_superuser, login_url=reverse_lazy('about')),  name='dispatch')
class AddCity(CreateView):
    """Class for adding the city by superuser"""
    form_class = AddCityForm
    template_name = 'cities/add_city.html'
    success_url = reverse_lazy('cities:add_city')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "City successfully added")
        return super(AddCity, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error during adding the city ")
        return super(AddCity, self).form_invalid(form)


@method_decorator(user_passes_test(lambda user: user.is_superuser, login_url=reverse_lazy('about')),  name='dispatch')
class EditCity(UpdateView):
    """Class for editing the city by superuser"""
    model = City
    form_class = AddCityForm
    template_name = 'cities/edit_city.html'
    pk_url_kwarg = 'city_pk'
    success_url = reverse_lazy('cities:view_cities')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "City successfully edited")
        return super(EditCity, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error during editing the city")
        return super(EditCity, self).form_invalid(form)


@method_decorator(user_passes_test(lambda user: user.is_superuser, login_url=reverse_lazy('about')),  name='dispatch')
class DeleteCity(DeleteView):
    """Class for deleting the city by superuser"""
    model = City
    pk_url_kwarg = 'city_pk'
    success_url = reverse_lazy('cities:view_cities')

    def get(self, request, *args, **kwargs):
        messages.success(self.request, "City successfully deleted")
        return self.post(request, *args, **kwargs)


class ViewTrainsFromCity(ListView):
    """Class for view  all trains for 30 days forward from city"""
    template_name = 'cities/trains_from_city.html'
    context_object_name = 'trains_from_city'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from_city = City.objects.get(pk=self.kwargs['from_city_pk'])
        context['from_city'] = from_city
        return context

    def queryset(self):
        return Train.objects.filter(
                    from_city_id=self.kwargs['from_city_pk'],
                    trip_start_time__range=[datetime.now(), datetime.now() + timedelta(days=30)],
                    trip_end_time__range=[datetime.now(), datetime.now() + timedelta(days=30)]
                )


class ViewTrainsToCity(ListView):
    """Class for view  all trains for 30 days forward to city"""
    template_name = 'cities/trains_to_city.html'
    context_object_name = 'trains_to_city'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        to_city = City.objects.get(pk=self.kwargs['to_city_pk'])
        context['to_city'] = to_city
        return context

    def queryset(self):
        return Train.objects.filter(
                    to_city_id=self.kwargs['to_city_pk'],
                    trip_start_time__range=[datetime.now(), datetime.now() + timedelta(days=30)],
                    trip_end_time__range=[datetime.now(), datetime.now() + timedelta(days=30)]
                )
