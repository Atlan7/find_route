from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import City
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


class AddCity(CreateView):
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


class EditCity(UpdateView):
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


class DeleteCity(DeleteView):
    model = City
    pk_url_kwarg = 'city_pk'
    success_url = reverse_lazy('cities:view_cities')

    def get(self, request, *args, **kwargs):
        messages.success(self.request, "City successfully deleted")
        return self.post(request, *args, **kwargs)
