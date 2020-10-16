from django.shortcuts import render
# Create your views here.
from .models import Car
def cars(request):
    cars = Car.objects.all().count()
    context = {
        "car":cars
    }
    print(cars)
    return render(request,'cars/cars.html',context)