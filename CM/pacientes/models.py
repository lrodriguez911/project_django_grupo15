from datetime import datetime
from django.db import models
from doctores.models import Doctor, Calendario, Usuario



# Create your models here.

class Paciente(models.Model):
    SEXO = [
        ("M",'Masculino'),
        ("F",'Femenino'),
        ("X",'No Binario'),
    ]
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE,primary_key=True, default=1)
    dni_pac = models.IntegerField(null=False, unique=True, default=1)
    sex = models.CharField(max_length= 1,choices=SEXO, default="M", null=True, blank=True)
    birthday = models.DateField(default='2000-01-01', null=True, blank=True)
    phone = models.CharField(max_length=22, default=None, null=True, blank=True)
    address = models.CharField(max_length=50, default=None, null=True, blank=False)
    vip = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    doctores=models.ManyToManyField(Doctor,through="Consulta")
    
    def __str__(self):
        return 'Usuario Paciente: ' + Usuario.first_name +' - DNI: ' +self.dni_pac
    
    def soft_delete(self):
        self.is_active=False
        self.updated=datetime.today
        super().save()
    
    def restore(self):
        self.is_active=True
        super().save()

    class Meta:
        verbose_name_plural = "Pacientes"



class Consulta(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    dni_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,default=1)
    dni_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,default=1)
    id_calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE,default=1)
    # date = models.DateField()
    # time_start = models.TimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    attended = models.BooleanField(default=False)
    observations = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return self.dni_paciente + "consulta con " + self.dni_doctor

    class Meta:
        verbose_name_plural = "Consultas"
