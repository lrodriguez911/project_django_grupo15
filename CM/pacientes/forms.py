from django import forms
from django.forms import ValidationError
import re

from django.contrib.auth.forms import UserCreationForm

from pacientes.models import Paciente, Consulta
from doctores.models import Especialidad, Doctor, Usuario
from django.core.exceptions import ValidationError  

def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError(
            "El nombre no puede contener números. %(valor)s",
            code="Invalid",
            params={"valor": value},
        )

def validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo electrónico inválido')
    return value


class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username','password1', 'password2']
        


class PacienteForm(forms.ModelForm):
      
    class Meta:
        model = Paciente
        
        fields = ['nombre','apellido', 'dni', 'sex', 'birthdate', 'phone_number', 'address', 'city' , 'postal','email', 'vip', ] 
        
        labels = ['Nombre: ','Apellido: ', 'DNI: ', 'Sexo: ', 'Fecha de Nacimiento: ', 'Telefono: ', 'Direccion: ', 'Ciudad: ' , 
                  'Codigo Postal: ','Email: ', 'Paciente Afiliado: ' ]
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'dni': forms.NumberInput(attrs={'class':'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control' } , choices= Doctor.SEXO),
            'birthdate' : forms.DateInput(attrs={"class": "form-control"}),
            'phone_number' :forms.TextInput(attrs={"class": "form-control"}),
            'address' :forms.TextInput(attrs={"class": "form-control"}),
            'city' :forms.TextInput(attrs={"class": "form-control"}),
            'postal' :forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'vip' : forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class ConsultaForm(forms.Form):
    ESPECIALITY = (
        Especialidad.objects.all().values_list("id_especiality", "name_especiality"),)
    DOCTORES = (
        Doctor.objects.all().values_list("license", "dni"),
    )
    """
    FIRST_NAME = {Paciente.objects.get(dni=Consulta.dni_paciente).first_name}
    nombre_paciente = forms.CharField(
        label="Nombre",
        max_length=50,
        validators=(solo_caracteres,),
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Luis Miguel"}
        ),
    )
    apellido_paciente = forms.CharField(
        label="Apellido",
        max_length=50,
        validators=(solo_caracteres,),
        widget=forms.TextInput(attrs={"class": "form-control pt-2", "placeholder": "Perez"}),
    ) """
    edad = forms.CharField(label="edad", max_length=3, widget=forms.NumberInput(
            attrs={"class": "form-control pt-2", "placeholder": "18"}
        ))
    observaciones = forms.CharField(
        label="Observaciones",
        max_length=500,
        widget=forms.Textarea(attrs={"rows": 5, "class": "form-control pt-2"}),
    )
    especialidad = forms.ChoiceField(
        label="Especialidad", 
        choices=ESPECIALITY, 
        initial=0, 
        widget=forms.Select(attrs={"class": "form-select"})
    )
    vip = forms.BooleanField(label="Paciente afiliado",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input pt-2", "value": 1}),)


consulta_form = ConsultaForm()

class ContactoForm(forms.Form):
    TIPO_CONSULTA = (
        ("", "-Seleccione motivo de Consulta-"),
        (1, "Turnos"),
        (2, "Cartilla"),
        (3, "Horarios"),
        (4, "Otros")
    )
    nombre = forms.CharField(
        label="Nombre y Apellido",
        max_length=100,
        validators=(solo_caracteres,),
        error_messages={"required": "Campo requerido"},
        widget=forms.TextInput(
            attrs={"class": "form-control", }
        ),
    )
    email = forms.EmailField(
        label="Email",
        max_length=100,
        validators=(validate_email,),
        error_messages={"required": "Campo requerido"},
        widget=forms.TextInput(attrs={"class": "form-control", "type": "email"}),
    )
    tipo_consulta = forms.ChoiceField(
        label="Tipo de consulta",
        choices=TIPO_CONSULTA,
        initial="0",
        error_messages={"required": "Campo requerido"},
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    asunto = forms.CharField(
        label="Asunto",
        max_length=100,
        error_messages={"required": "Campo requerido"},
        widget=forms.TextInput(attrs={"class": "form-control" }),
    )
    mensaje = forms.CharField(
        label="Mensaje",
        max_length=500,
        error_messages={"required": "Campo requerido"},
        widget=forms.Textarea(attrs={"rows": 5, "class": "form-control"}),
    )
   
    suscripcion = forms.BooleanField(
        label="Deseo suscribirme a las novedades del Centro Medico",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input", "value": 1}),
    )

    def clean_mensaje(self):
        data = self.cleaned_data["mensaje"]
        if len(data) < 10:
            raise ValidationError("Debes especificar mejor el mensaje que nos envias")
        return data

    def clean(self):
        cleaned_data = super().clean()
        asunto = cleaned_data.get("asunto")
        suscripcion = cleaned_data.get("suscripcion")


class CartillaEspecialidadForm(forms.Form):
    especialidad_sele = forms.ModelChoiceField(
        label="Seleccione la Especialidad a consultar  ",
        empty_label='Todas',
        required = False,
        queryset=Especialidad.objects.all(),
        widget = forms.Select(attrs = {"onchange" : "formProfesionales(this.value);","onload" : "formProfesionales(this.value)","class":"form-select"}))
    
    