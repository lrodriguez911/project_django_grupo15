from django.contrib import admin
from django.urls import path

from . import views # para importar las funciones que definimos

urlpatterns = [
    path('', views.index, name='inicio'),
   # path('quienes_somos/', views.quienes_somos, name='quienes_somos'),

   
    
]
