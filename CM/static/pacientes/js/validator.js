/* Validar formulario de contacto */

const nombre = document.getElementById("nombre");
const apellido = document.getElementById("nombre");
const email = document.getElementById("nombre");
const contrasena = document.getElementById("nombre");


let formulario = document
  .getElementById("contact-form")
  .addEventListener("submit", validarFormulario);

function validarFormulario(e) {
  e.preventDefault();
const nombre = document.getElementById("nombre").value;
const apellido = document.getElementById("apellido").value;
const email = document.getElementById("email").value;
const password = document.getElementById("password").value;

if(nombre.length == 0) {
  alert('No has escrito nada en el nombre');
  return;
}
if(apellido.length == 0) {
  alert('No has escrito nada en el apellido');
  return;
}
if(email.length == 0) {
  alert('No has escrito nada en el email');
  return;
}
if(password.length == 0) {
  alert('No has escrito nada en el password');
  return;
}
}

