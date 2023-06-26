from django.contrib import admin

from doctores.models import Doctor, Especialidad, Usuario, Calendario, Persona
from pacientes.models import Paciente, Consulta
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin


"""
from django.contrib.auth import get_user_model

Usuario = get_user_model()
"""

# Registro por defecto de Django para admin

admin.site.register(Doctor)
admin.site.register(Especialidad)
admin.site.register(Usuario)
admin.site.register(Calendario)

#Admin Personalizado heredando de AdminSite adming15


class CMAdminSite(admin.AdminSite):
    site_header = 'Administracion Centro Medico'
    site_title = 'Administracion superuser'
    index_title= 'Administracion del sitio CM'
    empty_value_display = 'No hay datos para visualizar'

# Personalizacion de visualizacion de modelos en el Admin de Django
class DoctorAdmin(admin.ModelAdmin): #Relacion onetoone con User
    model = Doctor
    verbose_name = 'Doctor'
    verbose_name_plural  = 'Doctores'
    
    list_display = [ 'apellido', 'nombre', 'dni', 'license' ,'especiality', 'get_username']  #campos que se muestran en change
    
    list_display_links = ['apellido']
    
    list_editable = [ 'nombre', 'dni', 'license' ,'especiality',]  #campos que se pueden editar en change
    
    
    search_fields = ['nombre' , 'apellido' , 'especiality']  #campos de busqueda
    
    list_filter = [ 'especiality', 'city', 'sex', 'apellido' ] #campos para filtros
    
    ordering = ['apellido' ]   
    
    @admin.display(description = 'Usuario')
    def get_username(sel, obj):
        return obj.user.username
    
    
    """
    fields = [ 'username','password', 'first_name', 'last_name', 'dni', 'license' ,'especiality', 'sex',
              'birthdate', 'phone_number', 'address' , 'city', 'postal', 'email' , 'is_active' ,  'date_joined']
    

    
    """
  
    
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = [ 'name_especiality',]
    search_fields = ['name_especiality']
    ordering = ["name_especiality"]
    #exclude = ('baja',)

    # listado que se quiere mostrar
    def get_queryset(self, request):
        query = super(EspecialidadAdmin, self).get_queryset(request)
       # filtered_query = query.filter(baja=False)
       # return filtered_query
       #return query

class CalendarioAdmin(admin.ModelAdmin):
   list_display = ['get_doctor', 'day' , 'hour', 'available']
   list_filter = ['id_doc__apellido']
   list_editable = ['day' , 'hour', 'available']
   ordering = ['id_doc__apellido','day','hour']
   
   @admin.display(description = 'Doctor' , ordering = 'id_doc__apellido')
   def get_doctor (self,obj):
       return obj.id_doc.apellido + ', ' + obj.id_doc.nombre

class ConsultaAdmin(admin.ModelAdmin):
   list_display = ['get_doctor', 'get_fecha', 'get_hora','get_paciente', 'attended', 'observations'] 
   list_filter = ['id_doctor__apellido' , 'id_paciente__apellido']

   ordering = ['id_doctor__apellido', 'id_calendario__day','id_calendario__hour']
   
   @admin.display(description = 'Doctor' )
   def get_doctor (self,obj):
       return obj.id_doctor.apellido + ', ' + obj.id_doctor.nombre   
   
   @admin.display(description = 'Paciente' )
   def get_paciente (self,obj):
       return obj.id_paciente.apellido + ', ' + obj.id_paciente.nombre   
   
   @admin.display(description = 'Fecha' )
   def get_fecha (self,obj):
       return obj.id_calendario.day   
   
   @admin.display(description = 'Horario' )
   def get_hora (self,obj):
       return obj.id_calendario.hour 
   
   #mostrar solo horarios de calendarios disponibles
   def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_calendario":
            kwargs["queryset"] = Calendario.objects.filter(available=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
   


    


#permite mostrar y editar modelos relacionados en línea dentro de la interfaz de administración de otro modelo     
class ConsultaInline(admin.TabularInline):
    model = Consulta

#agregar la funcionalidad de creación de instancias de Inscripcion
class PacienteAdmin(admin.ModelAdmin):
    verbose_name = 'Paciente'
    verbose_name_plural  = 'Pacientes'
    
    list_display = [ 'apellido', 'nombre', 'dni', 'birthdate' ,'vip', 'get_username']  #campos que se muestran en change
    
    list_display_links = ['apellido']
    
    list_editable = [ 'nombre', 'dni', 'birthdate' ,'vip',]  #campos que se pueden editar en change
    
    
    search_fields = ['nombre' , 'apellido', 'dni' ]  #campos de busqueda
    
    list_filter = [ 'apellido' , 'dni'] #campos para filtros
    
    ordering = ['apellido' ]   
    
    inlines = [
        ConsultaInline,
    ]
    
    @admin.display(description = 'Usuario')
    def get_username(sel, obj):
        return obj.user.username
    
    
   

#registros de modelos en Admin personalizado
sitio_admin = CMAdminSite(name='g15admin')
sitio_admin.register(Doctor, DoctorAdmin)
sitio_admin.register(Especialidad, EspecialidadAdmin)
sitio_admin.register(Usuario, UserAdmin)
sitio_admin.register(Group, GroupAdmin)
sitio_admin.register(Paciente,PacienteAdmin)
sitio_admin.register(Consulta,ConsultaAdmin)
sitio_admin.register(Calendario,CalendarioAdmin)






