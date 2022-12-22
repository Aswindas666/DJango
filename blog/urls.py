from django.urls import path
from blog import views


urlpatterns = [
    path('test/',views.Test,name='test'),
]