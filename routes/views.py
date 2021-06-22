from django.contrib import messages
from django.views.generic import FormView


from .models import Route
from .forms import FindRouteForm


class FindRoute(FormView):
    form_class = FindRouteForm
    template_name = 'routes/find_route.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Success')
        return super(FindRoute, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'No data for searching')
        return super(FindRoute, self).form_invalid(form)
