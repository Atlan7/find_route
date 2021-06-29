from django.shortcuts import render
from django.contrib import messages
from django.views.generic import FormView

from .forms import FindRouteForm
from .services import get_route


class FindRoute(FormView):
    form_class = FindRouteForm
    template_name = 'routes/find_route.html'
    context_object_name = 'routes'


    def post(self, request, template_name='routes/find_route.html'):
        form = FindRouteForm(request.POST)

        if form.is_valid():
            try:
                context = get_route(request, form)
            except ValueError as e:
                messages.error(self.request, e)
                return render(request, template_name, {'form': form})
            return render(request, template_name='routes/view_suitable_trains.html', context=context)
        return render(request, template_name, {'form': form})

    def form_valid(self, form):
        messages.success(self.request,'Routes')
        return super(FindRoute, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'No data for searching')
        return super(FindRoute, self).form_invalid(form)
