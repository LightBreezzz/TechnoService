gsap.registerPlugin(ScrollTrigger, ScrollSmoother)

// если мы не на устройстве с тачем (не на телефоне) Выполняются все плавные скроллы
if (ScrollTrigger.isTouch !==1){

    // мы передаем в метод объект с двумя компонентами
    ScrollSmoother.create({
        wrapper: '.wrapper',  // обертка, оболочка в которой действует плавный скролл
        content: '.content', // сам контент который будет плавать внутри
        smooth: 1.5,
        effects: true,
    }) 

    //анимации появления сразу при загрузке
    gsap.fromTo( '.amenities-title', {opacity:0}, {
        opacity: 1,
        duration: 1.1
    })

    gsap.fromTo( '.amenities-text__h1', {opacity:0, y: 30}, {
        opacity: 1,
        y: 0,
        duration: 1
    })
    gsap.fromTo( '.amenities-text__p', {opacity:0, y: 30}, {
        opacity: 1,
        y: 0,
        duration: 1,
        delay: 0.1
    })

    //анимации для каждого
    // let blocks = gsap.utils.toArray( '.content .ame-blocks')

    // blocks.forEach(block => {

    //     gsap.fromTo( block)
        
    // });

}