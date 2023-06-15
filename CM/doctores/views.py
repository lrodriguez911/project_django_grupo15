from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from doctores.forms import  DoctorForm
from doctores.models import Doctor

# Create your views here.
def home(request):
    return render(request, "doctores/home_doc.html")

def home_doc(request):
    return render(request, "doctores/home_doc.html")

def login_medico():
    documento = """<html><body><h1>Login Medico</h1></body></html>"""
    return HttpResponse(documento)

def calendario_turnos():
    documento = """<html><body><h1>Ver Turnos</h1></body></html>"""
    return HttpResponse(documento)

def ver_consulta():
    documento = """<html><body><h1>Ver resumen de consulta</h1></body></html>"""
    return HttpResponse(documento)

def ver_plantilla_medica():
    documento = """<html><body><h1>Ver la plantilla del paciente</h1></body></html>"""
    return HttpResponse(documento)

def ver_perfil():
    documento = """<html><body><h1>Ver mi perfil</h1></body></html>"""
    return HttpResponse(documento)



""" CONSULTORIO"""


def turnos_doctores(request):
    # queryset
    doctores = Doctor.objects.all()
    return render(request, "doctores/turnos_agendados.html", {"doctores": doctores})



def calendarios(request):
    # queryset
    doctores = Doctor.objects.all()
    return render(request, "doctores/calendarios.html", {"doctores": doctores})