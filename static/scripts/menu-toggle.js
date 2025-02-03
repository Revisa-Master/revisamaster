const menuToggle = document.querySelector('.cabecalho__nav__dropdown button');
const dropDownContent = document.querySelector('.cabecalho__nav__dropdown .content');

menuToggle.addEventListener('click', () => {
  dropDownContent.classList.toggle('active');
});