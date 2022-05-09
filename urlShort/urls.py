from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('shortener', views.makeshorturl),
    path('<str:shorturl>', views.redirecturl),
]
