from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView


from . import views  # para importar las funciones que definimos

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),

    path('contacto/', views.contacto, name='contacto'),
    
    path('pacientes/', views.home_pac, name='home_pac'),
    
    path('pacientes/turnos/', views.turnos, name='turnos'),

    path('pacientes/cartilla/', views.cartilla, name='cartilla'),
    path('pacientes/datos_pacientes/', views.datos_pacientes, name='datos_pacientes'),
    
    path('pacientes_CRUD/index/', views.pacientes_index,name='pacientes_index'),
    path('pacientes_CRUD/nuevo/', views.pacientes_nuevo,name='pacientes_nuevo'),
    path('pacientes_CRUD/editar//', views.pacientes_editar,name='pacientes_editar'),
    path('pacientes_CRUD/eliminar/', views.pacientes_eliminar,name='pacientes_eliminar'),
    
     path('cuentas/registrarse', views.CM_registrarse, name='registrarse'),
    
    #por defecto de django  - vistas basadas en clases  
    path('accounts/login/', auth_views.LoginView.as_view(
            template_name='pacientes/login.html',
            extra_context={'variable':''},
        )),
    path('accounts/logout/',
         views.CMLogoutView.as_view(), name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(success_url="/",), name='password_change'), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='lista_especialidades.html'), name='lista_especialidades'),
]

