from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    dni = models.IntegerField(primary_key=True,null=False,editable=True)

    pass

class Doctor(Usuario):
    SEXO = [
        ("M",'Masculino'),
        ("F",'Femenino'),
        ("X",'No Binario'),
    ]
    #dni = models.OneToOneField(Usuario, on_delete=models.CASCADE,primary_key=True)
    license = models.IntegerField(null=False, unique=True)
    sex = models.CharField(max_length= 1,choices=SEXO, default="M", null=True, blank=True)
    birthdate = models.DateField()
    phone_number = models.CharField(max_length=22, default=None, null=True, blank=True)
    especiality = models.ForeignKey('Especialidad', on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)   
    
    # turnos = models.ManyToManyField(Consulta,through='turnos')
    
    def __str__(self):
        return ' DR./DRA.' + self.first_name + ' ' + self.last_name
    
    class Meta():
        verbose_name_plural = 'Doctores'

class Especialidad(models.Model):
    id_especiality = models.IntegerField(primary_key=True)
    name_especiality = models.CharField(max_length=50,null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.name_especiality
    
    class Meta():
        verbose_name_plural = 'Especialidades'
    
class Calendario(models.Model):
    id_calendar = models.AutoField(primary_key=True)
    dni_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day = models.DateField()
    hour = models.TimeField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return 'Calendar of' + self.Doctor.last_name
    
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