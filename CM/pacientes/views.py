from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from pacientes.forms import ContactoForm, PacienteForm


# Create your views here.
def home(request):
    if(request.method=='POST'):
        contacto_form = ContactoForm(request.POST)    
        # mensaje='Hemos recibido tus datos'
        # acción para tomar los datos del formulario
        if(contacto_form.is_valid()):  
            messages.success(request,'consulta generada correctamente')          
        # acción para tomar los datos del formulario
        else:
            messages.warning(request,'Por favor revisa los errores en el formulario')
    else:
        pass
        # PacienteForm = PacienteForm() 
    context = {                             
                'consulta_form':PacienteForm,
            }
    return render(request, "./home.html",context)

def home_pac(request):
    Paciente_Form = PacienteForm()
    # lista_pacientes = ['lucas', 'fede']
    context = {                             
                'paciente_form':Paciente_Form,
            }
    return render(request, "./pacientes/home_pac.html", context)

def login_paciente():
    documento = """<html><body><h1>Login Paciente</h1></body></html>"""
    return HttpResponse(documento)

def calendario_turnos_agendados():
    documento = """<html><body><h1>Ver Turnos Agendados</h1></body></html>"""
    return HttpResponse(documento)

def ver_turnos_disponibles():
    documento = """<html><body><h1>Ver turnos disponibles</h1></body></html>"""
    return HttpResponse(documento)

def agendar_turno():
    documento = """<html><body><h1>Plantilla para agendar turno y poner datos</h1></body></html>"""
    return HttpResponse(documento)

def ver_perfil():
    documento = """<html><body><h1>Ver mi ficha medica</h1></body></html>"""
    return HttpResponse(documento)

def contacto(request):
    contacto_form = ContactoForm(request.POST)    
        # mensaje='Hemos recibido tus datos'
        # acción para tomar los datos del formulario
    if(contacto_form.is_valid()):  
            messages.success(request,'consulta generada correctamente')          
        # acción para tomar los datos del formulario
    else:
            messages.warning(request,'Por favor revisa los errores en el formulario')
    context = {                             
                'contacto_form':contacto_form,
            }        
    return render(request, "./pacientes/contacto.html",context)