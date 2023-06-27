const data = document.currentScript.dataset;
let doctores = JSON.parse(data?.doctores || null);
/* let especialidades = JSON.parse(data.especialidades); */

const listadoDoctores = document.getElementById('listado-doctores');
/* const selectEspecialidades = document.getElementById('select_especialidad');
const selectDoctores = document.getElementById('select_doctor'); */

function formProfesionales(value) {
    while(listadoDoctores.firstChild){
        listadoDoctores.removeChild(listadoDoctores.firstChild);
    }
    value ? docfilter = doctores.filter(doc => doc.fields.especiality == value) :
    docfilter = doctores;
    docfilter.map(doctor => {
        listadoDoctores.innerHTML += `<div class="col m-4">
    <div class="card h-100">
      <div class="card-body">
        <h5 class="card-title">
          Dr./ Dra. ${doctor.fields.nombre} ${doctor.fields.apellido}
        </h5>
        <p class="card-text">${doctor.fields.address}</p>
        <p class="card-text">${doctor.fields.phone_number}</p>
        <a href="#" class="btn btn-primary">Turno</a>
      </div>
    </div>
  </div>`})
};

function formProfesionalesMedicos(value) {
  /* while(listadoDoctores.firstChild){
    listadoDoctores.removeChild(listadoDoctores.firstChild);
} */
/* selectDoctores.innerHTML += `<option value="${doctor.fields.license}">hola</option>`
value ? docfilter = doctores.filter(doc => doc.fields.especiality == value) :
docfilter = doctores;
docfilter.map(doctor => {
  selectDoctores.innerHTML += `<option value="${doctor.fields.license}">${doctor.fields.nombre}</option>`}) */
};
