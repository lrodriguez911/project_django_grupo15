from django import forms
from django.forms import ValidationError
from pacientes.models import Paciente, Consulta
from doctores.models import Especialidad, Doctor


def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError(
            "El nombre no puede contener números. %(valor)s",
            code="Invalid",
            params={"valor": value},
        )


class PacienteForm(forms.ModelForm):
    dni_pac = forms.IntegerField(
        label="DNI",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True)
    first_name = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={"class": "form-control"}),)
    last_name = forms.CharField(
        label="Apellido",
        widget=forms.TextInput(attrs={"class": "form-control"}),)
    sex = forms.ChoiceField(
        label="Sexo",
        widget=forms.Select (attrs={"class": "form-control"}),)
    birthday = forms.DateField(
        label= "Fecha de Nacimiento",
        widget=forms.TextInput(attrs={"class": "form-control" ,}),
        required=True,)
    phone = forms.CharField(
        label="Teléfono",
        widget=forms.TextInput(attrs={"class": "form-control"}),)
    address = forms.CharField(
        label="Dirección",
        widget=forms.TextInput(attrs={"class": "form-control"}),)
    email = forms.EmailField(
        label="Correo Electronico",
        widget=forms.TextInput(attrs={"class": "form-control", "type": "email"}),)
    vip = forms.BooleanField(
        label="Paciente afiliado",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
        required=False,)
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),)
    is_active = forms.BooleanField(
        label="Activo",
        initial = True,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),)
    class Meta:
        model = Paciente
        fields = ['dni_pac','first_name', 'last_name', 'sex', 'birthday', 'phone', 'address', 'email', 'vip', 'password']


class ConsultaForm(forms.Form):
    ESPECIALITY = (
        Especialidad.objects.all().values_list("id_especiality", "name_especiality"),)
    DOCTORES = (
        Doctor.objects.all().values_list("license", "dni_dr"),
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
        error_messages={"required": "Campo requerido"},
        widget=forms.TextInput(attrs={"class": "form-control", "type": "email"}),
    )
    tipo_consulta = forms.ChoiceField(
        label="Tipo de consulta",
        choices=TIPO_CONSULTA,
        initial="2",
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


