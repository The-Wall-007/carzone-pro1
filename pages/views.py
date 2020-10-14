from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . models import Team

def home(request):
    teams = Team.objects.all()
    context = {
        'teams' : teams
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