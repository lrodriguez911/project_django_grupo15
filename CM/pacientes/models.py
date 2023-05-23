from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from doctores.models import Doctor
# Create your models here.

class Paciente(models.Model):
    dni = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    birthday = models.DateField()
    phone = PhoneNumberField(null=False, blank=False)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    vip = models.BooleanField(default=False)
    password = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title + '- by ' + self.name
    
    class Meta():
        verbose_name_plural = 'Pacientes'
    
class Consulta(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    dni_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    license_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time_start = models.TimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    attended = models.BooleanField(default=False)

    def __str__(self):
        return self.title + '- by ' + self.name
    
    class Meta():
        verbose_name_plural = 'Consultas'