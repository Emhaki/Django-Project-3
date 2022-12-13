const tick = document.querySelector('.wrapper');
const ticket = document.querySelector('.ticket');

btn.onclick = function () {
  if (tick.style.top == '200px') {
    tick.style.display = 'none';
    tick.style.top = '-730px';
    btn.style.animation = 'running';
    btn.innerHTML = 'PRINT TICKET';
  } else {
    tick.style.display = 'block';
    setTimeout(continueFunction, 10);
  }
};

function continueFunction() {
  tick.style.top = '200px';
  btn.style.animationPlayState = 'paused';
  btn.innerHTML = 'WAIT...';
  setTimeout(restartAnimation, 2000);

  btn.onclick = function () {
    takeTicket();
  };
}

function restartAnimation() {
  btn.style.animationPlayState = 'running';
  btn.innerHTML = 'TAKE A TICKET';
}

function takeTicket() {
  tick.style.transform = 'rotate(-90deg) translateY(-25%)';
  ticket.style.cursor = "pointer";
  ticket.addEventListener("click", () => {
    location.href = location.origin + "/articles/index/";
  })
}
