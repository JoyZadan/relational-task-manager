document.addEventListener('DOMContentLoaded', function() {
    // sidebar initialization
    let sidenav = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(sidenav);
    let slider = document.querySelectorAll('.slider');
    var instances = M.Slider.init('.slider');
  });

// const nav = document.querySelector('.nav');

// window.onscroll = function() {
//   var top = window.scrollY;
//   console.log(top);
//   if (top >= 100) {
//     nav.classList.add('active');
//   } else {
//     nav.classList.remove('active');
//   }
// }
