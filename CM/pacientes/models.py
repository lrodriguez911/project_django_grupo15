from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from doctores.models import Doctor, Calendario


# Create your models here.


class Paciente(models.Model):
    dni = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    sex = models.CharField(max_length=10, default="Male", null=True, blank=True)
    birthday = models.DateField(default='2000-01-01', null=True, blank=True)
    phone = PhoneNumberField(default=None, null=True, blank=True)
    address = models.CharField(max_length=50, default=None, null=True, blank=False)
    email = models.EmailField(default=None, null=True, blank=True)
    vip = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    password = models.CharField(max_length=50, default=dni)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name + self.lastname
    
    def soft_delete(self):
        self.active=True
        super().save()
    
    def restore(self):
        self.active=False
        super().save()

    class Meta:
        verbose_name_plural = "Pacientes"


class Consulta(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    dni_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    license_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    id_calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE,default=1)
    # date = models.DateField()
    # time_start = models.TimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    attended = models.BooleanField(default=False)
    observations = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return self.dni_paciente + "consulta con" + self.license_doctor

    class Meta:
        verbose_name_plural = "Consultas"
