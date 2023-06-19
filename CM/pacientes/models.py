from datetime import datetime
from django.db import models
from doctores.models import Doctor, Calendario, Usuario, Persona

from django.conf import settings



# Create your models here.

class Paciente(Persona):
    vip = models.BooleanField(default=False)
    doctores=models.ManyToManyField(Doctor,through="Consulta")
    
    def __str__(self):
        return 'Paciente: ' + self.nombre + ' ' + self.apellido +' - DNI: ' + str(self.dni) +' - Usuario: ' + self.user.username
    
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
        return self.id_paciente + "consulta con " + str(self.id_doctor)

    class Meta:
        verbose_name_plural = "Consultas"
