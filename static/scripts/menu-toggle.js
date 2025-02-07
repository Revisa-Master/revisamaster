// Seleciona o botão do dropdown e o menu
const dropdownToggle = document.querySelector('.dropdown__toggle');
const dropdownMenu = document.querySelector('.dropdown__menu');

// Adiciona o evento de clique ao botão do dropdown
dropdownToggle.addEventListener('click', () => {
    // Alterna a visibilidade do menu
    if (dropdownMenu.style.display === 'block') {
        dropdownMenu.style.display = 'none'; // Oculta o menu
    } else {
        dropdownMenu.style.display = 'block'; // Mostra o menu
    }
});