const txt = 'for the all future talented Artists';
let i = 0;
const speed = 100;

window.onload = function showWelcome() {
  if (i < txt.length) {
    document.querySelector('.welcome__sentence').innerHTML += txt.charAt(i);
    i++;
    setTimeout(showWelcome, speed);
  }
};
