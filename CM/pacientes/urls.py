from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views

from .views import (
    RegisterView,
    CustomLoginView,
    ResetPasswordView,
    ChangePasswordView,
    profile,
)
from pacientes.forms import LoginForm

from django.views.generic import TemplateView, ListView

from pacientes.views import especialidades_api

from . import views  # para importar las funciones que definimos


urlpatterns = [
    path("", views.home, name="home"),
    path("contacto/", views.contacto, name="contacto"),
    path("pacientes/", views.home_pac, name="home_pac"),
    path("pacientes/turnos/", views.turnos, name="turnos"),
    path("pacientes/cartilla/", views.cartilla, name="cartilla"),
    path("pacientes/datos_pacientes/", views.datos_pacientes, name="datos_pacientes"),
    path(
        "pacientes_CRUD/editar/<int:usuario_id>",
        views.pacientes_editar,
        name="pacientes_editar",
    ),
    path(
        "pacientes_CRUD/reactivar/<int:usuario_id>",
        views.pacientes_reactivar,
        name="pacientes_reactivar",
    ),
    path(
        "pacientes_CRUD/eliminar/<int:usuario_id>",
        views.pacientes_eliminar,
        name="pacientes_eliminar",
    ),
#     path(
#         "pacientes_CRUD/eliminar/confirmar/<int:usuario_id>",
#         views.pacientes_eliminar_confirmar,
#         name="pacientes_eliminar_confirmar",
#     ),
    path("profile/", profile, name="users-profile"),
    path(
        "register/",
        RegisterView.as_view(template_name="pacientes/register.html"),
        name="users-register",
    ),
    path(
        "login/",
        CustomLoginView.as_view(
            redirect_authenticated_user=True,
            template_name="pacientes/login.html",
            authentication_form=LoginForm,
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="pacientes/logout.html"),
        name="logout",
    ),
    path(
        "password-reset/",
        ResetPasswordView.as_view(template_name="pacientes/password_reset.html"),
        name="password_reset",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="pacientes/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="pacientes/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("password-change/", ChangePasswordView.as_view(), name="password_change"),
    path(
        "pacientes/lista_especialidades.html",
        views.lista_especialidades,
        name="lista_especialidades",
    ),
    path("especialidades/", especialidades_api, name="especialidades_api"),
    # path('pacientes/', ListaEspecalidades.as_view(template_name = "pacientes/lista_detalles.html"), name='Listaespecialidades'),
]
