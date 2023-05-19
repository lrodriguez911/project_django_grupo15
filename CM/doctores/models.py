from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

    
class Doctor(models.Model):
    license = models.IntegerField(primary_key=True)
    dni = models.IntegerField()
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    birthdate = models.DateField()
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True)
    especiality = models.ForeignKey('Especiality')
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title + '- by ' + self.name

class Especiality(models.Model):
    id_especiality = models.AutoField(primary_key=True)
    especiality = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.especiality
    
class Calendar(models.Model):
    id_calendar = models.AutoField(primary_key=True)
    doctor = models.ForeignKey('Doctor')
    day = models.DateField()
    hour = models.TimeField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return 'Calendar of' + self.doctor