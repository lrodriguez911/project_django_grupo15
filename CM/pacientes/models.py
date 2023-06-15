from datetime import datetime
from django.db import models
from doctores.models import Doctor, Calendario, Usuario, Persona



# Create your models here.

class Paciente(Persona):
    vip = models.BooleanField(default=False)
    doctores=models.ManyToManyField(Doctor,through="Consulta")
    
    def __str__(self):
        return 'Usuario Paciente: ' + self.first_name +' - DNI: ' +self.dni
    
    class Meta:
        verbose_name_plural = "Pacientes"



class Consulta(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,default=1)
    id_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,default=1)
    id_calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE,default=1)
    # date = models.DateField()
    # time_start = models.TimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    attended = models.BooleanField(default=False)
    observations = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return self.id_paciente + "consulta con " + self.id_doctor

    class Meta:
        verbose_name_plural = "Consultas"
