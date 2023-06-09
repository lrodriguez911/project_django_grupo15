from django.contrib import admin

from doctores.models import Doctor, Especialidad, Usuario, Calendario

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin


# Registro por defecto de Django para admin

admin.site.register(Doctor)
admin.site.register(Especialidad)
admin.site.register(Usuario)
#admin.site.register(Calendario)

#Admin Personalizado heredando de AdminSite adming15

class CMAdminSite(admin.AdminSite):
    site_header = 'Administracion Centro Medico'
    site_title = 'Administracion superuser'
    index_title= 'Administracion del sitio CM'
    empty_value_display = 'No hay datos para visualizar'

# Personalizacion de visualizacion de modelos en el Admin de Django
class DoctorAdmin(admin.ModelAdmin):
    pass
    """ fields = [ 'username','password', 'first_name', 'last_name', 'dni_dr', 'license' ,'especiality', 'sex',
              'birthdate', 'phone_number', 'address' , 'city', 'postal', 'email' , 'is_active' ,  'date_joined']
    
    list_display = ['username', 'first_name', 'last_name', 'dni_dr', 'license' ,'especiality']  #campos que se muestran en change
    list_display_links = ['dni_dr'] 
    list_editable = ['username', 'first_name', 'last_name',  'license' ,'especiality']  #campos que se pueden editar en change
    
    search_fields = ['first_name' , 'last_name' , 'username']  #campos de busqueda
            
    list_filter = [ 'especiality', 'city', 'sex', 'last_name'] #campos para filtros
    
    ordering = ["username"] """
    
    
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
        return query
"""
class CursoAdmin(admin.ModelAdmin):
    
    #modificar listados de foreingkey
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "categoria":
            kwargs["queryset"] = Categoria.objects.filter(baja=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

#permite mostrar y editar modelos relacionados en línea dentro de la interfaz de administración de otro modelo     
class InscripcionInline(admin.TabularInline):
    model = Inscripcion

#agregar la funcionalidad de creación de instancias de Inscripcion
class ComisionAdmin(admin.ModelAdmin):
    inlines = [
        InscripcionInline,
    ]
"""
#registros de modelos en Admin personalizado
sitio_admin = CMAdminSite(name='g15admin')
sitio_admin.register(Doctor, DoctorAdmin)
sitio_admin.register(Especialidad, EspecialidadAdmin)
sitio_admin.register(Usuario, UserAdmin)
sitio_admin.register(Group, GroupAdmin)
#sitio_admin.register(Calendario)




