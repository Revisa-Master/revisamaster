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

document.querySelectorAll('.hero-section-about__content')
    .forEach(element => {
        fadeIn.observe(element);
    });

document.querySelectorAll('.enter_to_left')
    .forEach(element => {
        leftObserver.observe(element);
    });

document.querySelectorAll('.enter_to_right')
    .forEach(element => {
        rightObserver.observe(element);
    });

    document.querySelectorAll('.button__effect_tag')
    .forEach(element => {
        buttonEffect.observe(element);
    });