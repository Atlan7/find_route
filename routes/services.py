from datetime import timedelta

from trains.models import Train


def get_trains_for_route(from_city, to_city, initial_period_for_route, end_route_period):
    """Trying to get trains for route with necessary period of route"""
    trains = Train.objects.select_related('from_city', 'to_city').filter(
                    from_city_id=from_city.id,
                    to_city_id=to_city.id,
                    trip_start_time__range=[initial_period_for_route, end_route_period + timedelta(days=1)],
                    trip_end_time__range=[initial_period_for_route, end_route_period + timedelta(days=1)]
                )
    return trains


def get_route(request, form) -> dict:
    """Trying to get routes with needed start and end cities."""
    context = {'form': form}
    from_city = form.cleaned_data['from_city']
    to_city = form.cleaned_data['to_city']
    initial_period_for_route = form.cleaned_data['initial_period_for_route']
    end_route_period  = form.cleaned_data['end_route_period']
    trains_for_route = get_trains_for_route(
                from_city,
                to_city,
                initial_period_for_route,
                end_route_period
             )


    print(*trains_for_route)
    context['trains_for_route'] = trains_for_route
    context['cities'] = {'from_city': from_city.name,'to_city': to_city.name}

    if not trains_for_route:
        raise ValueError("No suitable route. Try to input another paramets.")

    return context

