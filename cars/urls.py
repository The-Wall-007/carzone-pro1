from django.urls import path
from .views import cars,carDetails
urlpatterns = [

    path('',cars,name='cars'),
    
]
