const menuToggle = document.querySelector('.dropdown button');
const dropDownContent = document.querySelector('.dropdown .content');

menuToggle.addEventListener('click', () => {
  dropDownContent.classList.toggle('active');
});