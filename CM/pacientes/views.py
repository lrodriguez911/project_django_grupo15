from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from pacientes.forms import PacienteForm
from pacientes.forms import ContactoForm

from pacientes.models import Paciente

from datetime import datetime
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    """
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
        ContactForm = ContactoForm()
        
    context = {                             
                'consulta_form':PacienteForm,
            }
            
    return render(request, "./home.html",context)
    """
    return render(request, "./home.html")


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
            messages.success(request,'Hemos recibido tus datos')
            mensaje=f"De: {contacto_form.cleaned_data['nombre']} <{contacto_form.cleaned_data['email']}>\n Asunto: {contacto_form.cleaned_data['asunto']}\n Mensaje: {contacto_form.cleaned_data['mensaje']}"
            mensaje_html=f"""
                <p>De: {contacto_form.cleaned_data['nombre']} <a href="mailto:{contacto_form.cleaned_data['email']}">{contacto_form.cleaned_data['email']}</a></p>
                <p>Asunto:  {contacto_form.cleaned_data['asunto']}</p>
                <p>Mensaje: {contacto_form.cleaned_data['mensaje']}</p>
            """
            asunto="CONSULTA DESDE LA PAGINA - "+contacto_form.cleaned_data['asunto']
            """ send_mail(
                asunto,
                mensaje,
                settings.EMAIL_HOST_USER,
                [settings.RECIPIENT_ADDRESS],
                fail_silently=False,
                html_message=mensaje_html
            ) """
                
        # acción para tomar los datos del formulario
    else:
            messages.warning(request,'Por favor revisa los errores en el formulario')
    context = {                             
                'contacto_form':contacto_form,
            }        
    return render(request, "./pacientes/contacto.html",context)


""" CRUD DE PACIENTES PARA SU REGISTRACION"""

def pacientes_index(request):
    #queryset
    pacientes = Paciente.objects.filter(active=False)
    return render(request,'pacientes_CRUD/index.html',{'pacientes':pacientes})

def pacientes_nuevo(request):
#forma de resumida de instanciar un formulario basado en model con los
    #datos recibidos por POST si la petición es por POST o bien vacio(None)
    #Si la petición es por GET
    formulario = PacienteForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha registrado el paciente correctamente')          
        return redirect('pacientes_index')
    return render(request,'pacientes/pacientes_CRUD/nuevo.html',{'formulario':formulario})


def pacientes_editar(request,dni):
    try:
        paciente = Paciente.objects.get(pk=dni)
    except Paciente.DoesNotExist:
        return render(request,'pacientes/404_pac.html')

    formulario = PacienteForm(request.POST or None,request.FILES or None,instance=paciente)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se han editado los datos del paciente correctamente')          
        return redirect('pacientes_index')
    return render(request,'pacientes/pacientes_CRUD/editar.html',{'formulario':formulario})

def pacientes_eliminar(request,dni):
    try:
        curso = Paciente.objects.get(pk=dni)
    except Paciente.DoesNotExist:
        return render(request,'pacientes/404_pac.html')
    Paciente.soft.delete()
    messages.success(request,'Se ha dado de baja el paciente correctamente') 
    return redirect('pacientes_index')

