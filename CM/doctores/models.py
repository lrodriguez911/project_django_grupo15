from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    pass

class Doctor(Usuario):
    SEXO = [
        ("M",'Masculino'),
        ("F",'Femenino'),
        ("X",'No Binario'),
    ]
    #dni = models.OneToOneField(Usuario, on_delete=models.CASCADE,primary_key=True)
    # user = models.OneToOneField(Usuario, on_delete=models.CASCADE,, default=1)
    dni_dr = models.IntegerField(null=False, unique=True,primary_key=True, default=1,verbose_name="DNI")
    license = models.IntegerField(null=False, unique=True, default=1, verbose_name="Licencia Profesional")
    sex = models.CharField(max_length= 1,choices=SEXO, default="M", null=True, blank=True, verbose_name="Sexo")
    birthdate = models.DateField(verbose_name="Fecha de Nacimiento")
    phone_number = models.CharField(max_length=22, default=None, null=True, blank=True, verbose_name="Telefono")
    especiality = models.ForeignKey('Especialidad', on_delete=models.CASCADE, verbose_name="Especialidad")
    address = models.CharField(max_length=50, verbose_name="Direccion")
    city=models.CharField(max_length=50, verbose_name="Ciudad")
    postal=models.CharField(max_length=10, verbose_name="Codigo Postal")
    updated = models.DateTimeField(auto_now=True) 
    
    
    # turnos = models.ManyToManyField(Consulta,through='turnos')
    
    def __str__(self):
        return  "Dr.: "+self.first_name +" "+self.last_name + " - Licencia Profesional: "+ str(self.license) + " - Usuario: " + self.username
    
    class Meta():
        verbose_name_plural = 'Doctores'

class Especialidad(models.Model):
    id_especiality = models.AutoField(primary_key=True, verbose_name="ID Especialidad")
    name_especiality = models.CharField(max_length=50,null=False, verbose_name="Especialidad")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
   
    def __str__(self):
        return self.name_especiality
    
    class Meta():
        verbose_name_plural = 'Especialidades'
    
class Calendario(models.Model):
    id_calendar = models.AutoField(primary_key=True, verbose_name="ID Calendario")
    dni_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="DNI Dr")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, verbose_name="Vigente")
    
    def __str__(self):
        return 'Calendario del Dr. ' + Doctor.first_name +" "+Doctor.last_name + " - Licencia Profesional: "+ str(Doctor.license) + " - Usuario: " + Doctor.username
    
    class Meta():
        verbose_name_plural = 'Calendarios'

class CalendarioTurno(models.Model):
    id_calendar = models.ForeignKey(Calendario, on_delete=models.CASCADE)
    day = models.DateField(verbose_name="Fecha")
    hour = models.TimeField(verbose_name="Horario")
    available = models.BooleanField(default=True, verbose_name="Disponible")

