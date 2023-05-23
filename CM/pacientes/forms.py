from django import forms
from django.forms import ValidationError




def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError(
            "El nombre no puede contener números. %(valor)s",
            code="Invalid",
            params={"valor": value},
        )


class PacienteForm(forms.Form):
    TYPE_CONSULT = (
        ("", "-Select-"),
        (1, "Clinico"),
        (2, "Pediatra"),
        (3, "Ginecologo"),
        (4, "Traumatologo"),
    )
    
    nombre = forms.CharField(
        label="Nombre",
        max_length=50,
        validators=(solo_caracteres,),
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Luis Miguel"}
        ),
    )
    apellido = forms.CharField(
        label="Apellido",
        max_length=50,
        validators=(solo_caracteres,),
        widget=forms.TextInput(attrs={"class": "form-control pt-2", "placeholder": "Perez"}),
    )
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
        choices=TYPE_CONSULT, 
        initial=1, 
        widget=forms.Select(attrs={"class": "form-select"})
    )
    subscribe = forms.BooleanField(label="Paciente afiliado",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input pt-2", "value": 1}),)



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
            attrs={"class": "form-control", "placeholder": "Solo letras"}
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
        widget=forms.TextInput(attrs={"class": "form-control"}),
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

        if suscripcion and asunto and "suscripcion" not in asunto:
            msg = "Debe agregar la palabara 'suscripcion' al asunto."
            self.add_error("asunto", msg)
