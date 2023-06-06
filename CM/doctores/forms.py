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


class DoctorForm(forms.ModelForm):
    ESPECIALITY = (
        Especialidad.objects.all().values_list("id_especiality", "name_especiality"),)
    dni_doc = forms.IntegerField(
        label="DNI",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True)
    first_name = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={"class": "form-control"}),)
    last_name = forms.CharField(
        label="Apellido",
        widget=forms.TextInput(attrs={"class": "form-control"}),)
    license = forms.IntegerField(
        label="Licencia",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True)
      
    especialidad = forms.ChoiceField(
        label="Especialidad", 
        choices=ESPECIALITY, 
        initial=0, 
        widget=forms.Select(attrs={"class": "form-select"})
    )
    
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),)
    is_active = forms.BooleanField(
        label="Activo",
        initial = True,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),)
    class Meta:
        model = Doctor
        fields = ['dni_doc','first_name', 'last_name', 'license', 'password']


