from django.contrib import admin

from doctores.models import Doctor, Especialidad


# Registro por defecto de Django
admin.site.register(Doctor)
admin.site.register(Especialidad)

#Admin Personalizado heredando de AdminSite
"""
class CMAdminSite(admin.AdminSite):
    site_header = 'Administracion Centro Medico'
    site_title = 'Administracion superuser'
    index_title= 'Administracion del sitio'
    empty_value_display = 'No hay datos para visualizar'

# Personalizacion de visualizacion de modelos en el Admin de Django
class DoctorAdmin(admin.ModelAdmin):
    list_display = ( 'username','password' , 'first_name', 'last_name', 'dni_dr', 'license' ,'especiality', 'sex', 'birthdate', 'phone_number', 'address' , 'city', 'postal', 'email' , 'is_active' , 'updated', 'date_joined')
    list_editable = ( 'username','password' , 'first_name', 'last_name', 'dni_dr', 'license' ,'especiality', 'sex', 'birthdate', 'phone_number', 'address' , 'city', 'postal', 'email' , 'is_active' )
    list_filter = ( 'username','dni_dr', 'license' ,'especiality')
    search_fields = ('username','dni_dr', 'license' ,'especiality')
    
    

class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ( 'nombre',)
    exclude = ('baja',)

    #modificacion del listado que se quiere mostrar
    def get_queryset(self, request):
        query = super(CategoriaAdmin, self).get_queryset(request)
        filtered_query = query.filter(baja=False)
        return filtered_query

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

#registros de modelos en Admin personalizado
sitio_admin = CacAdminSite(name='cacadmin')
sitio_admin.register(Estudiante,EstudianteAdmin)
sitio_admin.register(Proyecto)
sitio_admin.register(Categoria,CategoriaAdmin)
sitio_admin.register(Curso,CursoAdmin)
sitio_admin.register(Comision,ComisionAdmin)
sitio_admin.register(Usuario,UserAdmin)
sitio_admin.register(Group, GroupAdmin)
# admin.site.register(Curso,CursoAdmin)

"""

