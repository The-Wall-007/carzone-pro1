from django.urls import path
from .views import cars,carDetails,searchView
urlpatterns = [

    path('',cars,name='cars'),
    path('search',searchView,name='search'),
    
]
