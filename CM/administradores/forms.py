from django import forms
from django.forms import ValidationError




def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError(
            "El nombre no puede contener números. %(valor)s",
            code="Invalid",
            params={"valor": value},
        )


class DoctorForm(forms.Form):
    ESPECIALIDAD = (
        ("", "-Select-"),
        (1, "Clinico"),
        (2, "Pediatra"),
        (3, "Ginecologo"),
        (4, "Traumatologo"),
        (5, "Psicologo"),
        (6, "Psiquiatra"),
        (7, "Dermatologo"),
        (7, "Diagnosticoporimagenes"),
        (7, "Otorrinolaringologo"),
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
