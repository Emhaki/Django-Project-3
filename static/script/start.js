const txt = 'for all future talented Artists';
let start_i = 0;
const speed = 50;
window.onload = function showWelcome() {
  if (start_i < txt.length) {
    document.querySelector('.welcome__sentence').innerHTML += txt.charAt(start_i);
    start_i++;
    setTimeout(showWelcome, speed);
  }
};