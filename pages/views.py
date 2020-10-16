from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . models import Team
from cars.models import Car

def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    cars = Car.objects.order_by('-created_date')
    context = {
        'teams' : teams,
        'featured_cars' : featured_cars,
        'cars' : cars,
    }
    return render(request,'pages/home.html',context)

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