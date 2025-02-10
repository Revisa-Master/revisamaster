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
    CAPTURANDO SELETORES NO HTML HERO SECTION E SECTION 2
============================================================ */

document.querySelectorAll('.section-content-2__container, .hero-section__hero-text')
    .forEach(element => {
        fadeIn.observe(element);
    });

document.querySelectorAll('.button__effect_tag')
    .forEach(element => {
        buttonEffect.observe(element);
    });

/*=============================================
    CAPTURANDO SELETORES NO HTML SECTION 3
===============================================*/

document.querySelectorAll('.section-content-3__container__service-block-left-1')
    .forEach(element => {
        leftObserver.observe(element);
    });

document.querySelectorAll('.section-content-3__container__service-block-left-2')
    .forEach(element => {
        leftObserver.observe(element);
    });


document.querySelectorAll('.section-content-3__container__service-block-left-3')
    .forEach(element => {
        leftObserver.observe(element);
    });    

//------------------------------------------------------------------------------------//
//------------------------------------------------------------------------------------//

document.querySelectorAll('.section-content-3__container__service-block-right-1')
    .forEach(element => rightObserver.observe(element));

document.querySelectorAll('.section-content-3__container__service-block-right-2')
    .forEach(element => rightObserver.observe(element));

document.querySelectorAll('.section-content-3__container__service-block-right-3')
    .forEach(element => rightObserver.observe(element));