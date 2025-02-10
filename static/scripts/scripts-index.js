/*=============================================
    CRIANDO CALLBACKS PARA ANIMAÇÕES
===============================================*/

const leftObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('left__to__right');
            leftObserver.unobserve(entry.target); // Stop observing once animated
        }
    });
});

const rightObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('right__to__left');
            rightObserver.unobserve(entry.target); // Stop observing once animated
        }
    });
});

const fadeIn = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade__in');
            rightObserver.unobserve(entry.target); // Stop observing once animated
        }
    });
});

const buttonEffect = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('button__effect');
            rightObserver.unobserve(entry.target); // Stop observing once animated
        }
    });
});

/*=========================================================
    CAPTURANDO SELETORES QUE VÃO RECEBER O FADE-IN
============================================================ */

document.querySelectorAll('.overlay, .section-content-2__third-column, .section-content-2__second-column, .animation__text__fade-in, .block')
    .forEach(element => {
        fadeIn.observe(element);
    });

document.querySelectorAll('.section-content-2__first-column')
    .forEach(element => {
        leftObserver.observe(element);
    });

document.querySelectorAll('.section-content-2__fourth-column')
    .forEach(element => {
        rightObserver.observe(element);
    });

    document.querySelectorAll('.button__effect_tag')
    .forEach(element => {
        buttonEffect.observe(element);
    });