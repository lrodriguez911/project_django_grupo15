from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse , JsonResponse
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from django.views import View
from django.core import serializers

from pacientes.forms import ContactoForm, RegisterForm , PacienteForm , CartillaEspecialidadForm , LoginForm
from .forms import PacienteForm, UpdateUserForm
from pacientes.models import Paciente
from doctores.models import Doctor, Especialidad,Usuario

from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin


from doctores.models import Especialidad
from django import template

register = template.Library()

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


# Create your views here.

class ListaEspecalidades(ListView):
    model = Especialidad
    template_name ='pacientes/turnos.html'
    context_object_name = 'especialidades'

def home(request):
    return render(request, "./pacientes/home.html")


#@permission_required('pacientes.ver_modulo_paciente')
def home_pac(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            messages.success(
                request, f'Tu cuenta fue creada con éxito! Ya te podes loguear en el sistema.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, './pacientes/home_pac.html', {'form': form, 'title': 'registrese aquí'})


def CM_registrarse(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            messages.success(
                request, f'Su cuenta fue creada con éxito! Ya puede iniciar Sesion en el sistema.')
            return redirect('login')
    else:
        form = RegisterForm()
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


def pacientes_editar(request, usuario_id):
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



def pacientes_eliminar(request, usuario_id):
    try:
        paciente = Paciente.objects.get(user__id=usuario_id)
    except Paciente.DoesNotExist:
        return render(request,'pacientes/404_pac.html')    
    
    if(request.method=='POST'):
        paciente.soft_delete()
        return redirect('home_pac')
    else:
        formulario = PacienteForm(instance=paciente)
        if formulario.is_valid():
            paciente.soft_delete()
            messages.success(request, "Se ha dado de baja el paciente correctamente")
            return redirect('home_pac')
    return render(request,'pacientes/pacientes_CRUD/eliminar.html',{'form':formulario , 'paciente':paciente})

def paciente_alta(request, usuario_id):
    try:
        paciente = Paciente.objects.get(user__id=usuario_id)
        paciente.is_active=True
        paciente.save()
        return redirect(request,'pacientes/home.html')
    except Paciente.DoesNotExist:
        return render(request,'pacientes/404_pac.html')  

def pacientes_eliminar_confirmar(request, usuario_id):
    try:
        paciente = Paciente.objects.get(user__id=usuario_id)
        paciente.is_active=False
        paciente.save()
        return redirect(request,'pacientes/home.html')
    except Paciente.DoesNotExist:
        return render(request,'pacientes/404_pac.html')    
    
    



""" TURNOS PACIENTES"""


def turnos(request):
    # queryset
    pacientes = Paciente.objects.all()
    return render(request, "pacientes/turnos.html", {"pacientes": pacientes})


""" CARTILLA"""


def cartilla(request):
    
    """ @register.filter
    def en_especialidad(things, especialidad):
        return things.filter(especialidad=especialidad) """
    # queryset
    especialidades = Especialidad.objects.all()
    doctores = serializers.serialize("json", Doctor.objects.all())
    # doctores = Doctor.objects.all()
    form = CartillaEspecialidadForm(request.POST)
    contexto = {"especialidades": especialidades , "form" : form, "doctores": doctores}
    
    return render(request, "pacientes/cartilla.html", contexto)


"""Para borrar cuando registro este ok"""


def datos_pacientes(request):
    # queryset
    pacientes = Paciente.objects.all()
    return render(request, "pacientes/datos_pacientes.html", {"pacientes": pacientes})



def lista_especialidades(request):
    Especialidades = Especialidad.objects.all()
    return render(request, 'pacientes/lista_especialidades.html', {'Especialidades': Especialidades})
    
def especialidades_api(request):
    especialidades = Especialidad.objects.all().values('id_especiality', 'name_especiality')
    return JsonResponse({'especialidades': list(especialidades)})

#######################################################
#Autenticacion
#######################################################
@login_required
def profile(request):
    if request.method == 'POST':
        # user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = PacienteForm(request.POST, request.FILES, instance=request.user.paciente)

        # and profile_form.is_valid()
        if profile_form.is_valid() :
            # user_form.save()
            profile_form.save()
            messages.success(request, 'Su usuario a sido creado correctamente')
            return redirect(to='users-profile')
    else:
        # user_form = UpdateUserForm(instance=request.user)
        profile_form = PacienteForm(instance=request.user.paciente)

    # , 'profile_form': profile_form 'user_form': user_form, 
    return render(request, 'pacientes/profile.html', {'profile_form': profile_form})


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'pacientes/register.html'
    
    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='login')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            usernameForm = form.cleaned_data.get("username")
            usuario = Usuario.objects.get(username=usernameForm)
            try:
                paciente = Paciente.objects.get(user_id=usuario.id)
                print(paciente + "pac")
                print(usuario.id)
            except:
                pacienteCreado = Paciente.objects.create(user_id=usuario.id)
                print(pacienteCreado + "creado")
                messages.success(request, f'Usuario creado para {usernameForm}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})
    
    
# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)    
    
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'pacientes/password_reset.html'
    email_template_name = 'pacientes/password_reset_email.html'
    subject_template_name = 'pacientes/password_reset_subject.html'
    success_message = "Le hemos enviado instrucciones por correo electrónico para establecer su contraseña. " \
                      "Si la cuenta de correo ingresada existe, deberia recibirlas a la brevedad" \
                      " Si no recibe un correo, " \
                      "por favor asegúrese de haber ingresado la dirección con la que se registró y verifique su carpeta de correo no deseado."
    success_url = reverse_lazy('users-home')    



class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'pacientes/change_password.html'
    success_message = "Contraseña cambiada con exito"
    success_url = reverse_lazy('home')


