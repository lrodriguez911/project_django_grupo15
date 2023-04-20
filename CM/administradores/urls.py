from django.contrib import admin
from django.urls import path

from . import views # para importar las funciones que definimos

urlpatterns = [
    path('', views.home, name='home'),
    path('administradores/', views.home_adm, name='home_adm'),
    
]
