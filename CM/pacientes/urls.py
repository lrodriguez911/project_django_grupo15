from django.contrib import admin
from django.urls import path

from . import views  # para importar las funciones que definimos

urlpatterns = [
    path('', views.home, name='home'),

    path('contacto/', views.contacto, name='contacto'),
    
    path('pacientes/', views.home_pac, name='home_pac'),
    
    path('pacientes/turnos/', views.turnos, name='turnos'),
    path('pacientes/cartilla/', views.cartilla, name='cartilla'),
    path('pacientes/datos_pacientes/', views.datos_pacientes, name='datos_pacientes'),
    
    path('pacientes_CRUD/index/', views.pacientes_index,name='pacientes_index'),
    path('pacientes_CRUD/nuevo/', views.pacientes_nuevo,name='pacientes_nuevo'),
    path('pacientes_CRUD/editar/', views.pacientes_editar,name='pacientes_editar'),
    path('pacientes_CRUD/eliminar/', views.pacientes_eliminar,name='pacientes_eliminar'),
]
