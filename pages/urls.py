from django.urls import path
from .views import home,car,service,contact,about


urlpatterns = [

    path('', home, name='home'),
    #path('carz', car, name='car'),
    path('service', service, name='service'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
]
