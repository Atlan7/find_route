from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Train
from .forms import AddTrainForm


class ViewTrains(ListView):
    model = Train
    template_name = 'trains/view_trains.html'
    context_object_name = 'trains'


class AddTrain(CreateView):
    form_class = AddTrainForm
    template_name = 'trains/add_train.html'
    success_url = reverse_lazy('trains:add_train')

    def is_valid(self, form):
        form.save()
        messages.success(self.request, "Train successfully added")
        return super(AddTrain, self).form_valid(form)

    def is_invalid(self, form):
        messages.error(self.request, "Error during adding train")
        return super(AddTrain, self).form_invalid(form)


class ViewTrain(DetailView):
    model = Train
    template_name = 'trains/view_train.html'
    context_object_name = 'train'
    pk_url_kwarg = 'train_pk'
