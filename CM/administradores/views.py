from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def admin_login():
    documento = """<html><body><h1>Admin Login</h1></body></html>"""
    return HttpResponse(documento)

def ver_doctores():
    documento = """<html><body><h1>Lista de Doctores</h1></body></html>"""
    return HttpResponse(documento)

def ver_pacientes():
    documento = """<html><body><h1>Lista de Pacientes</h1></body></html>"""
    return HttpResponse(documento)

def calendario_turnos():
    documento = """<html><body><h1>Calendario Con turnos tomados y disponibles</h1></body></html>"""
    return HttpResponse(documento)