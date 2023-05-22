from django.contrib import admin
from django.urls import path

from . import views # para importar las funciones que definimos

urlpatterns = [
    path('', views.home, name='home'),
    path('pacientes/', views.home_pac, name='home_pac'),
    path('contacto/', views.contacto, name='contacto'),
]
