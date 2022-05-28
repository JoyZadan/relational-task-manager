document.addEventListener('DOMContentLoaded', function() {
    // sidebar initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
    // modal initialization
    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);
    // datepicker initialization
    var datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
      format: "dd mmmm, yyyy",
      i18n: {done: "Select"}
    });
    // select initialization
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);
  });


// navbar changes background colour on scroll
const nav = document.querySelector('.nav');

window.onscroll = function() {
  var top = window.scrollY;
  console.log(top);
  if (top >= 50) {
    nav.classList.add('active');
  } else {
    nav.classList.remove('active');
  }
}
