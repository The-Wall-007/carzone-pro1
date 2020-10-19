from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . models import Team
from cars.models import Car

def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model',flat=True).distinct()
    body_style = Car.objects.values_list('body_style',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    print(year_search)
    states = Car.objects.values_list('state',flat=True).distinct()

    context = {
        'teams' : teams,
        'featured_cars' : featured_cars,
        'cars' : cars,
        'model_search' : model_search,
        'year_search' : year_search,
        'body_style' : body_style,
        'states' : states,
    }
    return render(request,'pages/index.html',context)

def car(request):
    return render(request,'pages/cars.html')

def service(request):
    return render(request,'pages/services.html')

def contact(request):
    return render(request,'pages/contact.html')

def about(request):
    teams = Team.objects.all()
    context = {
        'teams' : teams
    }
    return render(request,'pages/about.html',context)