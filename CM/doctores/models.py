from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# from pacientes.models import Consulta

# Create your models here.

    
class Doctor(models.Model):
    license = models.IntegerField(primary_key=True)
    dni = models.IntegerField(null=False, unique=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    birthdate = models.DateField()
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True)
    especiality = models.ForeignKey('Especialidad', on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # turnos = models.ManyToManyField(Consulta,through='turnos')
    
    def __str__(self):
        return ' DR./DRA.' + self.name + self.lastname
    
    class Meta():
        verbose_name_plural = 'Doctores'

class Especialidad(models.Model):
    id_especiality = models.IntegerField(primary_key=True)
    name_especiality = models.CharField(max_length=50,null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.especiality
    
    class Meta():
        verbose_name_plural = 'Especialidades'
    
class Calendario(models.Model):
    id_calendar = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day = models.DateField()
    hour = models.TimeField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return 'Calendar of' + self.doctor
    
    class Meta():
        verbose_name_plural = 'Calendarios'


"""  ESPECIALIDADES = [
        (1,'Clinico'),
        (2,'Pediatra'),
        (3,'Ginecologo'),
        (4,'Traumatologo'),
        (5,'Endocrinologo'),
        (6,'Cardiologo'),
        (7,'Otorrinolaringologo'),
        (8,'Reumatologo'),
        (9,'Gerontologo'),
        (10,'Neurologo'),
        (11,'Psicologo'),
        (12,'Oftalmologo'),
        (13,'Oncologo'),
        (14, 'Psiquiatra'),
    ] """