// Инициализация Swiper для секции направлений работы
document.addEventListener('DOMContentLoaded', function() {
    // Проверяем, есть ли на странице контейнер слайдера.
    // На внутренних страницах его нет, и без этой проверки Swiper выбрасывает ошибку в консоль.
    const swiperContainer = document.querySelector('.directions-swiper');
    if (!swiperContainer) {
        return;
    }

    const directionsSwiper = new Swiper(swiperContainer, {
        // Автопрокрутка каждые 10 секунд
        autoplay: {
            delay: 10000,
            disableOnInteraction: false,
        },
        
        // Зацикливание слайдов
        loop: true,
        
        // Эффект перехода
        effect: 'slide',
        
        // Скорость перехода
        speed: 800,
        
        // Пагинация (точки)
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        
        // Адаптивность
        breakpoints: {
            320: {
                slidesPerView: 1,
                spaceBetween: 20
            },
            768: {
                slidesPerView: 1,
                spaceBetween: 30
            },
            992: {
                slidesPerView: 1,
                spaceBetween: 40
            }
        }
    });
});