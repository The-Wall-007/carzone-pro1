from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars,2)
    page = request.GET.get('page')
    page_cars = paginator.get_page(page)
    context = {
        "cars":page_cars
    }
    print(cars)
    return render(request,'cars/cars.html',context)

def carDetails(request,id):
    car = get_object_or_404(Car,id=id)
    context = {
        "car":car
    }
    return render(request,'pages/car-details.html',context)