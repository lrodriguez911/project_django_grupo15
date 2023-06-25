from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from pacientes.models import Paciente
from doctores.models import Usuario


@receiver(post_save, sender=Usuario)
def create_paciente(sender, instance, created, **kwargs):
    if created:
        Paciente.objects.create(user=instance)


@receiver(post_save, sender=Usuario)
def save_paciente(sender, instance, **kwargs):
    instance.paciente.save()