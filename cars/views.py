from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.
def cars(request):
    model_search = Car.objects.values_list('model',flat=True).distinct()
    body_style = Car.objects.values_list('body_style',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    states = Car.objects.values_list('state',flat=True).distinct()
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars,2)
    page = request.GET.get('page')
    page_cars = paginator.get_page(page)
    context = {
        "cars":page_cars,
        'model_search' : model_search,
        'year_search' : year_search,
        'body_style' : body_style,
        'states' : states,

    }
    print(cars)
    return render(request,'cars/cars.html',context)

def carDetails(request,id):
    car = get_object_or_404(Car,id=id)
    context = {
        "car":car
    }
    return render(request,'pages/car-details.html',context)

def searchView(request):
    # qs = Car.objects.all()
    # search = request.GET.get('keyword', None)
    # if search is not None:
    #         if isinstance(search,int):
    #             qs = Car.objects.filter(Q(car_title=search)).distinct()
    #         else:
    #             qs = Car.objects.filter(
    #                 Q(car_title=search)
    #                 | Q(model=search)).distinct()
    # context = {"cars":qs}
    # print(search)

    model_search = Car.objects.values_list('model',flat=True).distinct()
    body_style = Car.objects.values_list('body_style',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    states = Car.objects.values_list('state',flat=True).distinct()

    cars = Car.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword :
            cars = cars.filter(Q(description__icontains=keyword))
    if 'location' in request.GET:
        state = request.GET['location']
        if state :
            cars = cars.filter(Q(state=state))
    if 'model' in request.GET:
        model = request.GET['model']
        if model :
            cars = cars.filter(Q(model=model))
    if 'year' in request.GET:
        year = request.GET['year']
        if year :
            cars = cars.filter(Q(year=year))
    if 'Type' in request.GET:
        Type = request.GET['Type']
        if Type :
            cars = cars.filter(Q(body_style=Type))
    if 'min-price' in request.GET:
        min_price = request.GET['min-price']
        max_price = request.GET['max-price']
        if max_price :
            cars = cars.filter(Q(price__gte=min_price),Q(price__lte=max_price))

   
    context = {"cars":cars,
    "model_search" : model_search,
    "body_style" : body_style,
    "year_search" : year_search,
    "states" : states,
    }
    return render(request,'cars/search.html',context)