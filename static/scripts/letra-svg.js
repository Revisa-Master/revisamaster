document.addEventListener("DOMContentLoaded", function() {
    const svg = document.querySelector('svg');
    const textElements = svg.querySelectorAll('text');
    textElements.forEach(el => {
      el.style.fontFamily = "'Questrial', sans-serif";
    });
  });