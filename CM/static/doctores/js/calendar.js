  const d = new Date();
  const actualYear = d.getFullYear(); // 2023
  const locale = 'es';
  const mesesamostrar = 3;
  const intlForMonths = new Intl.DateTimeFormat(locale, { month: 'long' });

  const onClick = (event) => {
    document.getElementById("result").innerHTML = ("     "+event.srcElement.innerHTML+" de "+event.srcElement.parentElement.parentElement.querySelector("h2").innerText);
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