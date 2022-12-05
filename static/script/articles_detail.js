const detail = document.querySelector('.article__detail');
const close = document.querySelector('.detail__close');
const image = document.querySelector('.detail__img');

function resizeImage(img) {
  img.style.width = '70%';
  detail.style.display = 'block';
}

function restoreImage() {
  image.style.width = '100%';
  detail.style.display = 'none';
}
