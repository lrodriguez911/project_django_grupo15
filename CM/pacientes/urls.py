from django.contrib import admin
from django.urls import path

from . import views  # para importar las funciones que definimos

urlpatterns = [
    path('', views.home, name='home'),

    path('contacto/', views.contacto, name='contacto'),
    
    path('pacientes/', views.home_pac, name='home_pac'),
    path('pacientes_CRUD/index', views.pacientes_index,name='pacientes_index'),
    path('pacientes_CRUD/nuevo/', views.pacientes_nuevo,name='pacientes_nuevo'),
    path('pacientes_CRUD/editar/<int:dni>', views.pacientes_editar,name='pacientes_editar'),
    path('pacientes_CRUD/eliminar/<int:dni>', views.pacientes_eliminar,name='pacientes_eliminar'),
]
