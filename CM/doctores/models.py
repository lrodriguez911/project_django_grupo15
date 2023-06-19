from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.

class Usuario(AbstractUser):
    pass

class Persona(models.Model):
    SEXO = [
        ("M",'Masculino'),
        ("F",'Femenino'),
        ("X",'No Binario'),
    ]
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, null=False, blank=False, verbose_name="Apellido")
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name="Email")
    dni = models.IntegerField(null=False, unique=True, default=1, verbose_name="DNI")
    sex = models.CharField(max_length= 1,choices=SEXO, default="M", null=True, blank=True, verbose_name="Sexo")
    birthdate = models.DateField(verbose_name="Fecha de Nacimiento")
    phone_number = models.CharField(max_length=22, default=None, null=True, blank=True, verbose_name="Telefono")
    address = models.CharField(max_length=50, verbose_name="Direccion")
    city=models.CharField(max_length=50, verbose_name="Ciudad")
    postal=models.CharField(max_length=10, verbose_name="Codigo Postal")
    updated = models.DateTimeField(auto_now=True) 
    
    class Meta:
        abstract = True
            

    
    def soft_delete(self):
        self.user.is_active=False
        self.updated=datetime.today
        super().save()
    
    def restore(self):
        self.user.is_active=True
        super().save()
    
class Doctor(Persona):  
    license = models.IntegerField(null=False, unique=True, default=1, verbose_name="Licencia Profesional") 
    especiality = models.ForeignKey('Especialidad', on_delete=models.CASCADE, verbose_name="Especialidad")
       
    def __str__(self):
        return  "Dr.: "+self.nombre +" "+self.apellido + " - Licencia Profesional: "+ str(self.license) + " - Usuario: " + self.user.username
    
    class Meta():
        verbose_name_plural = 'Doctores'

class Especialidad(models.Model):
    id_especiality = models.AutoField(primary_key=True, verbose_name="ID Especialidad")
    name_especiality = models.CharField(max_length=50,null=False, unique=True, verbose_name="Especialidad")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
   
    def __str__(self):
        return self.name_especiality
    
    class Meta():
        verbose_name_plural = 'Especialidades'
    
class Calendario(models.Model):
    id_calendar = models.AutoField(primary_key=True, verbose_name="ID Calendario")
    id_doc = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="ID Dr")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    day = models.DateField(verbose_name="Fecha")
    hour = models.TimeField(verbose_name="Horario")
    available = models.BooleanField(default=True, verbose_name="Disponible")

    def __str__(self):
        #return 'Calendario del Dr. ' + Doctor.first_name +" "+Doctor.last_name + " - Licencia Profesional: "+ str(Doctor.license) + " - Usuario: " + Doctor.username
        return 'Calendario del Dr. ' + " - Licencia Profesional: "+ str(Doctor.license) 
    class Meta():
        verbose_name_plural = 'Calendarios'


