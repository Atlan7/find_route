from django import template

register = template.Library()


@register.filter()
def subtract_date(value, arg):
    return value - arg
