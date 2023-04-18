from django.db import models

# Create your models here.

class Paciente(models.Model):
    dni = models.IntegerField()
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    vip = models.BooleanField(default=False)
    # user = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '- by ' + self.name