from django.urls import path
from .views import home,car,service,contact,about
from cars.views import carDetails

urlpatterns = [

    path('', home, name='home'),
    #path('carz', car, name='car'),
    path('service', service, name='service'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('car-details/<id>/', carDetails, name='car-details'),
 ]
