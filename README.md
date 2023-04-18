# project_django_grupo15
Proyecto Centro Medico
Integrantes del grupo:
  Lucas Rodriguez
  Federico Zatterra
  Ignacio Agustin Martinez Barrio
  Alejandra Benaim
  
paciente (superclase)
	particular
	obra social	


doctor (superclase)
	internos 
	externos	

administradores


sedes (superclase)



Table Persona {
  dni varchar [pk]
  nombre varchar
  apellido varchar
  sexo varchar(1)
  fecha_nacimiento date
  telefono varchar
  email varchar
}

Table Especialidad {
  id_especialidad varchar [pk]
  especialidad varchar
}

Table Medico {
  matricula varchar [pk]
  especialidad varchar [ref: > Especialidad.id_especialidad] 
  dni_persona varchar [ref: > Persona.dni]
}

Table Paciente {
  dni_persona varchar [pk, ref: > Persona.dni]
  obra_social varchar
}

Table Administrativo {
  dni_persona varchar [pk, ref: > Persona.dni]
  nivel varchar
}

Table Turno {
  id_turno int [pk, increment]
  fecha date
  hora_inicio time
  duracion int
}

Table TurnoMedico {
  id_turno int [ref: > Turno.id_turno]
  matricula_medico varchar [ref: > Medico.matricula]
  dni_paciente varchar [ref: > Paciente.dni_persona]
}

Table Calendario {
  fecha date [pk]
  matricula_medico varchar [pk, ref: > Medico.matricula]
  hora_inicio time
  duracion int
}

Table Consulta {
  id_consulta int [pk, increment]
  dni_paciente varchar [ref: > Paciente.dni_persona]
  matricula_medico varchar [ref: > Medico.matricula]
  fecha date
  hora_inicio time
  duracion int
}

Table CartillaMedicos {
  plan varchar
  Provincia varchar
  Localidad varchar
  matricula varchar [pk, ref: > Medico.matricula]
}

Table Autorizacion {
  id_autorizacion int [pk, increment]
  dni_paciente varchar [ref: > Paciente.dni_persona]
  dni_administrativo varchar [ref: > Administrativo.dni_persona]
  fecha date
  autorizado bool
}