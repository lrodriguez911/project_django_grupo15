from django.contrib import admin

from pacientes.models import Paciente, Consulta

from doctores.admin import CMAdminSite

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

# Registro por defecto de Django

admin.site.register(Paciente)
admin.site.register(Consulta)



# Personalizacion de visualizacion de modelos en el Admin de Django
class PacienteAdmin(admin.ModelAdmin): #Relacion onetoone con User
    model = Paciente
    verbose_name = 'Paciente'
    verbose_name_plural  = 'Pacientes'
    
    list_display = [ 'dni', 'vip', ]  #campos que se muestran en change
    
    """
    fields = [ 'username','password', 'first_name', 'last_name', 'dni', 'license' ,'especiality', 'sex',
              'birthdate', 'phone_number', 'address' , 'city', 'postal', 'email' , 'is_active' ,  'date_joined']
    

    list_display = ['username', 'first_name', 'last_name', 'dni', 'license' ,'especiality']  #campos que se muestran en change
    list_display_links = ['dni'] 
    
    list_editable = ['username', 'first_name', 'last_name',  'license' ,'especiality']  #campos que se pueden editar en change
    
    
    search_fields = ['first_name' , 'last_name' , 'username']  #campos de busqueda
    """
            
    #list_filter = [ 'especiality', 'city', 'sex', 'last_name' ] #campos para filtros
    
   # ordering = ['last_name' ]    
   
#registros de modelos en Admin personalizado
sitio_admin = CMAdminSite(name='g15admin')
sitio_admin.register(Paciente, PacienteAdmin) 