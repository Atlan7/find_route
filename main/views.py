from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    name = 'Nikita'
    return render(request, 'base.html', context={'name': name})