from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse , JsonResponse
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404

from pacientes.forms import ContactoForm, RegistrarUsuarioForm , PacienteForm
from pacientes.models import Paciente
from doctores.models import Doctor, Especialidad,Usuario

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from doctores.models import Especialidad
# Create your views here.
def home(request):
    return render(request, "./pacientes/home.html")


def home_pac(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            messages.success(
                request, f'Tu cuenta fue creada con éxito! Ya te podes loguear en el sistema.')
            return redirect('login')
    else:
        form = RegistrarUsuarioForm()
    return render(request, './pacientes/home_pac.html', {'form': form, 'title': 'registrese aquí'})

"""
#autenticacion manual
def login(request):
 if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            nxt = request.GET.get("next", None)
            if nxt is None:
                return redirect('inicio')
            else:
                return redirect(nxt)
        else:
            messages.error(request, f'Cuenta o password incorrecto, realice el login correctamente')
    form = AuthenticationForm()
    return render(request, 'publica/login.html', {'form': form, 'title': 'Log in'}) 
    return render(request, "./pacientes/login.html",)
"""    


def CM_registrarse(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            messages.success(
                request, f'Tu cuenta fue creada con éxito! Ya te podes loguear en el sistema.')
            return redirect('login')
    else:
        form = RegistrarUsuarioForm()
    return render(request, 'pacientes/registrarse.html', {'form': form, 'title': 'registrese aquí'})

class CMLogoutView(LogoutView):
    # next_page = 'inicio'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Se ha cerrado la session correctamente.')
        return response

def calendario_turnos_agendados():
    documento = """<html><body><h1>Ver Turnos Agendados</h1></body></html>"""
    return HttpResponse(documento)


def ver_turnos_disponibles():
    documento = """<html><body><h1>Ver turnos disponibles</h1></body></html>"""
    return HttpResponse(documento)


def agendar_turno(request):
    documento = """<html><body><h1>Plantilla para agendar turno y poner datos</h1></body></html>"""
    return HttpResponse(documento)


def ver_perfil():
    documento = """<html><body><h1>Ver mi ficha medica</h1></body></html>"""
    return HttpResponse(documento)


def contacto(request):
    if request.method == "POST":
        contacto_form = ContactoForm(request.POST)
        # acción para tomar los datos del formulario
        if contacto_form.is_valid():
            messages.success(request, "Su consulta fue generada correctamente")
            # return redirect("home") para volver al home luego de la consulta
            # envio de mail con consulta
            """
            mensaje=f"De: {contacto_form.cleaned_data['nombre']} <{contacto_form.cleaned_data['email']}>\n Asunto: {contacto_form.cleaned_data['asunto']}\n Mensaje: {contacto_form.cleaned_data['mensaje']}"
            mensaje_html=f
                <p>De: {contacto_form.cleaned_data['nombre']} <a href="mailto:{contacto_form.cleaned_data['email']}">{contacto_form.cleaned_data['email']}</a></p>
                <p>Asunto:  {contacto_form.cleaned_data['asunto']}</p>
                <p>Mensaje: {contacto_form.cleaned_data['mensaje']}</p>
                        
            asunto="CONSULTA DESDE LA PAGINA - "+contacto_form.cleaned_data['asunto']
                send_mail(
                asunto,
                mensaje,
                settings.EMAIL_HOST_USER,
                [settings.RECIPIENT_ADDRESS],
                fail_silently=False,
                html_message=mensaje_html
            ) """
        else:
            messages.warning(request, "Por favor revise los errores en el formulario")
    else:
        contacto_form = ContactoForm()

    context = {
        "contacto_form": ContactoForm,
    }
    return render(request, "./pacientes/contacto.html", context)


""" CRUD DE PACIENTES PARA SU REGISTRACION"""


def pacientes_index(request):
    # queryset
    pacientes = Paciente.objects.filter(is_active=True)
    return render(
        request, "pacientes/pacientes_CRUD/index.html", {"pacientes": pacientes}
    )


def pacientes_nuevo(request):
    # forma de resumida de instanciar un formulario basado en model con los
    # datos recibidos por POST si la petición es por POST o bien vacio(None)
    # Si la petición es por GET
    formulario = RegistrarUsuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, "Se ha registrado el paciente correctamente")
        return redirect("pacientes_index")
    return render(
        request, "pacientes/pacientes_CRUD/nuevo.html", {"formulario": formulario}
    )


def pacientes_editar(request, usuario_id=5):
    
    try:
        paciente = Paciente.objects.get(user__id=usuario_id)
    except Paciente.DoesNotExist:
        return render(request,'pacientes/404_pac.html')

    if(request.method=='POST'):
        formulario = PacienteForm(request.POST,instance=paciente)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se han editado los datos del paciente correctamente")
            return redirect('home_pac')
    else:
        formulario = PacienteForm(instance=paciente)
    return render(request,'pacientes/pacientes_CRUD/editar.html',{'form':formulario})

  

def pacientes_eliminar(request):
    # queryset
    pacientes = Paciente.objects.all()
    return render(request, "pacientes/datos_pacientes.html", {"pacientes": pacientes})
    """
    try:
        paciente = get_object_or_404(Paciente, pk=1)
    except Paciente.DoesNotExist:
        return render(request, "pacientes/404_pac.html")
    paciente.soft_delete()
    messages.success(request, "Se ha dado de baja el paciente correctamente")
    return redirect("pacientes_index")
    """

""" TURNOS PACIENTES"""


def turnos(request):
    # queryset
    pacientes = Paciente.objects.all()
    return render(request, "pacientes/turnos.html", {"pacientes": pacientes})


""" CARTILLA"""


def cartilla(request):
    # queryset
    especialidades = Especialidad.objects.all()
        
    contexto = {"especialidades": especialidades }
    return render(request, "pacientes/cartilla.html", contexto )


"""Para borrar cuando registro este ok"""


def datos_pacientes(request):
    # queryset
    pacientes = Paciente.objects.all()
    return render(request, "pacientes/datos_pacientes.html", {"pacientes": pacientes})



def lista_especialidades(request):
    especialidades = Especialidad.objects.all()
    return render(request, '/CM/templates/pacientes/lista_especialidades.html', {'especialidades': especialidades})


