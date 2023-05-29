# Create your tests here.
import random
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.test import TestCase
from doctores.models import Doctor, Calendario


class Command(BaseCommand):
    help = 'Crea registros al azar de turnos médicos en el calendario'
    cantidadturnos = 5
    def handle(self, *args, **options):
        # Obtener todos los doctores
        doctors = Doctor.objects.all()

        # Generar turnos para cada doctor
        for doctor in doctors:
            for _ in range(self.cantidadturnos):  # Generar x turnos por cada doctor
                # Generar una fecha aleatoria dentro de los próximos 30 días
                start_date = datetime.now().date() + timedelta(days=random.randint(1, 30))
                start_time = datetime.strptime("09:00", "%H:%M").time()  # Hora de inicio: 09:00
                end_time = datetime.strptime("17:00", "%H:%M").time()  # Hora de fin: 17:00
                duration = timedelta(minutes=30)  # Duración de cada turno: 30 minutos

                # Generar una hora de inicio aleatoria en intervalos de 30 minutos
                total_slots = int((datetime.combine(datetime.today(), end_time) - datetime.combine(datetime.today(), start_time)).seconds / duration.seconds)
                slot_index = random.randint(0, total_slots - 1)
                start_datetime = datetime.combine(start_date, start_time) + timedelta(minutes=slot_index * 30)
                end_datetime = start_datetime + duration

                # Crear el turno en la base de datos
                Calendario.objects.create(doctor=doctor, start_datetime=start_datetime, end_datetime=end_datetime)

        self.stdout.write(self.style.SUCCESS('Se han creado los turnos al azar.'))

