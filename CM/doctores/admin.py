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
    
    list_display = [ 'apellido', 'nombre', 'dni', 'license' ,'especiality', ]  #campos que se muestran en change
    
    list_display_links = ['apellido']
    
    list_editable = [ 'nombre', 'dni', 'license' ,'especiality',]  #campos que se pueden editar en change
    
    
    search_fields = ['nombre' , 'apellido' , 'especiality']  #campos de busqueda
    
    list_filter = [ 'especiality', 'city', 'sex', 'apellido' ] #campos para filtros
    
    ordering = ['apellido' ]   
    
    
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
   list_filter = ['id_doc']
   ordering = ['id_doc','day','hour']

   
    
"""
class CursoAdmin(admin.ModelAdmin):
    
    #modificar listados de foreingkey
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "categoria":
            kwargs["queryset"] = Categoria.objects.filter(baja=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
"""

#permite mostrar y editar modelos relacionados en línea dentro de la interfaz de administración de otro modelo     
class ConsultaInline(admin.TabularInline):
    model = Consulta

#agregar la funcionalidad de creación de instancias de Inscripcion
class PacienteAdmin(admin.ModelAdmin):
    inlines = [
        ConsultaInline,
    ]

#registros de modelos en Admin personalizado
sitio_admin = CMAdminSite(name='g15admin')
sitio_admin.register(Doctor, DoctorAdmin)
sitio_admin.register(Especialidad, EspecialidadAdmin)
sitio_admin.register(Usuario, UserAdmin)
sitio_admin.register(Group, GroupAdmin)
sitio_admin.register(Paciente,PacienteAdmin)
sitio_admin.register(Consulta)
sitio_admin.register(Calendario,CalendarioAdmin)






