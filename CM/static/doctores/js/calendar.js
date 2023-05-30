  const d = new Date();
  const actualYear = d.getFullYear(); // 2023
  const locale = 'es';
  const mesesamostrar = 3;
  const intlForMonths = new Intl.DateTimeFormat(locale, { month: 'long' });
  
  const onClick = (event) => {
    // Obtener el elemento contenedor
    if (event.srcElement.localName == "li"){
    
      var contenedor = document.getElementById('result');
      var valoranterior = document.getElementById('texto');
      var valoranterior2 = document.getElementById('boton');
      
      if (valoranterior){
        var cont = valoranterior.parentNode;
        var cont2 = valoranterior2.parentNode; 
        cont.removeChild(valoranterior);
        cont2.removeChild(valoranterior2);
      } else {}

      // document.getElementById("result").innerHTML = ("     "+event.srcElement.innerHTML+" de "+event.srcElement.parentElement.parentElement.querySelector("h2").innerText);
      // Crear elementos
      // var textbox = document.getElementById("result").createElement ("     "+event.srcElement.innerHTML+" de "+event.srcElement.parentElement.parentElement.querySelector("h2").innerText); //.createElement('input');
      var textbox = document.createElement('input');
      textbox.setAttribute('type', 'text');
      textbox.setAttribute('id', 'texto'); // Asignar ID al cuadro de texto

      textbox.value = event.srcElement.innerHTML+" de "+event.srcElement.parentElement.parentElement.querySelector("h2").innerText
      // document.createElement('input') = event.srcElement.innerHTML+" de "+event.srcElement.parentElement.parentElement.querySelector("h2").innerText;
      // textbox.textContent = event.srcElement.innerHTML+" de "+event.srcElement.parentElement.parentElement.querySelector("h2").innerText

      var button = document.createElement('button');
      button.setAttribute('id','boton')
      button.textContent =  'Confirmar';

      // Agregar elementos al documento
        contenedor.appendChild(textbox);
        contenedor.appendChild(button);

        // Función de envío
      function enviarTexto() {
        var texto = textbox.value;
        console.log('Texto ingresado: ' + texto);
        // Aquí puedes agregar la lógica para enviar el texto a un servidor, mostrarlo en la página, etc.
      }

      // Asociar función de envío al evento click del botón
      button.addEventListener('click', enviarTexto);
    } else {

    }
  }
  window.addEventListener('click', onClick);


  /* const months = [...Array(6).keys()] */
  //const months = [3, 4, 5, 6, 7, 8]
  const months = [];
  month = d.getMonth();
  for (let i = 0; i < mesesamostrar; i++) {
    months.push(Number(month)+i);
  }

  const intlForWeeks = new Intl.DateTimeFormat(locale, { weekday: 'short' })
  const weekDays = [...Array(7).keys()].map((dayIndex) =>
  //intlForWeeks.format(new Date(2023, 4, dayIndex + 1))
    intlForWeeks.format(new Date(actualYear, months[0], dayIndex + 1))
  )

  const calendar = months.map((monthIndex) => {
    const nextMonthIndex = (monthIndex + 1) % 12
    const daysOfMonth = new Date(actualYear, nextMonthIndex, 0).getDate()
    const monthName = new Date(actualYear, monthIndex, 1).toLocaleString('default', { month: 'long' });
    const startsOn = new Date(actualYear, monthIndex, 1).getDay()

    return {
      daysOfMonth,
      monthName,
      startsOn
    }
  })

  const html = calendar
    .map(({ daysOfMonth, monthName, startsOn }) => {
      const days = [...Array(daysOfMonth).keys()]
      const firstDayAttributes = `class='first-day' style='--first-day-start: ${startsOn}'`
      const htmlDaysName = weekDays
        .map((dayName) => `<li class='day-name'>${dayName}</li>`)
        .join('')
      const htmlDays = days
        .map(
          (day, index) =>
            `<li ${index === 0 ? firstDayAttributes : ''}>${day + 1}</li>`
        )
        .join('')
      return `<div class='col-4' id='hache2'><h2>${monthName} ${actualYear}</h2><ol style="cursor: pointer;">
      ${htmlDaysName}${htmlDays}</ol></div></h2>`

    })
    .join('')

  document.getElementById('calendar').innerHTML = html