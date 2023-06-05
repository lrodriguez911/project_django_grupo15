/* Validar formulario de contacto */

let nombre_apellido = document.getElementById("nombre");
let formulario = document
  .getElementById("contact-form")
  .addEventListener((e) => {
    e.preventDefault();
    console.log(e.target.value);
  });
console.log(nombre_apellido);
