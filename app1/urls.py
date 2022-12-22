from django.urls import path
from .views import Home,Next,index


urlpatterns = [
    path('',Home, name='Home'),
    path('next/',Next,name='Next'),
    path('index/',index,name='Index'),
]