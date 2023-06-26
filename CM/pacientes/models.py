from datetime import datetime
from django.db import models
from doctores.models import Doctor, Calendario, Usuario, Persona

from django.conf import settings
from PIL import Image



# Create your models here.

class Paciente(Persona):
    is_active = models.BooleanField(default=True)
    vip = models.BooleanField(default=False)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    doctores=models.ManyToManyField(Doctor,through="Consulta")
    
    def __str__(self):
        return 'Paciente: ' + self.nombre + ' ' + self.apellido +' - DNI: ' + str(self.dni) 
    
    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
        # img.save(self.avatar.path)

    def restore(self):
        self.user.is_active=True
        super().save()

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
        return self.id_paciente.nombre +" " +self.id_paciente.apellido + " consulta con Dr: " + self.id_doctor.nombre+ " " +self.id_doctor.apellido
    class Meta:
        verbose_name_plural = "Consultas"
