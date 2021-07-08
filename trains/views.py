from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

from .models import Train
from .forms import AddTrainForm


class ViewTrains(ListView):
    model = Train
    template_name = 'trains/view_trains.html'
    context_object_name = 'trains'
    paginate_by = 10

    def get_queryset(self):
        return Train.objects.all().select_related('from_city', 'to_city')


class ViewTrain(DetailView):
    model = Train
    template_name = 'trains/view_train.html'
    context_object_name = 'train'
    pk_url_kwarg = 'train_pk'


@method_decorator(user_passes_test(lambda user: user.is_superuser, login_url=reverse_lazy('about')),  name='dispatch')
class AddTrain(CreateView):
    """Class for adding the train by superuser"""
    form_class = AddTrainForm
    template_name = 'trains/add_train.html'
    success_url = reverse_lazy('trains:add_train')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Train successfully added")
        return super(AddTrain, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error during adding train")
        return super(AddTrain, self).form_invalid(form)


@method_decorator(user_passes_test(lambda user: user.is_superuser, login_url=reverse_lazy('about')),  name='dispatch')
class EditTrain(UpdateView):
    """Class for editing the train by superuser"""
    model = Train
    form_class = AddTrainForm
    template_name = 'trains/edit_train.html'
    pk_url_kwarg = 'train_pk'
    success_url = reverse_lazy('trains:view_trains')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Train successfully edited")
        return super(EditTrain, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error during adding train")
        return super(EditTrain, self).form_invalid(form)


@method_decorator(user_passes_test(lambda user: user.is_superuser, login_url=reverse_lazy('about')),  name='dispatch')
class DeleteTrain(DeleteView):
    """Class for deleting the train by superuser"""
    model = Train
    pk_url_kwarg = 'train_pk'
    success_url = reverse_lazy('trains:view_trains')

    def get(self, request, *args, **kwargs):
        messages.success(self.request, "Train successfully deleted")
        return self.post(request, *args, **kwargs)
