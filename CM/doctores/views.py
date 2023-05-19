from django.shortcuts import render
from django.http import HttpResponse
from .models import Consultas

# Create your views here.
def home(request):
    consultas = Consultas.objects.all()

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
