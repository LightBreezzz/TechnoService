// Инициализация функционала каталога
document.addEventListener('DOMContentLoaded', function() {
    // Проверяем, есть ли на странице каталог
    const catalogSection = document.querySelector('.catalog-section');
    if (!catalogSection) {
        return;
    }

    // Обработка клика по кнопке "В корзину" в карточке
    const addToCartButtons = document.querySelectorAll('.catalog-card__button');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation(); // чтобы не открывать модалку при клике по кнопке

            const card = this.closest('.catalog-card');
            const title = card.querySelector('.catalog-card__title').textContent;
            const price = card.querySelector('.catalog-card__price-value').textContent;

            // Здесь будет логика добавления в корзину
            // В будущем можно добавить запрос к бэкенду
            console.log('Товар добавлен в корзину:', {
                title: title,
                price: price
            });

            // Визуальная обратная связь
            const originalText = this.querySelector('.catalog-card__button-text').textContent;
            this.querySelector('.catalog-card__button-text').textContent = 'Добавлено!';
            this.style.background = '#00c950';

            setTimeout(() => {
                this.querySelector('.catalog-card__button-text').textContent = originalText;
                this.style.background = '#00c2d2';
            }, 2000);
        });
    });

    // Работа с модальными окнами каталога
    const body = document.body;
    const modalOverlays = document.querySelectorAll('.catalog-modal-overlay');

    function openModalById(productId) {
        const modal = document.querySelector(`.catalog-modal-overlay[data-modal-id="${productId}"]`);
        if (!modal) {
            return;
        }

        modal.classList.add('catalog-modal-overlay--visible');
        body.classList.add('catalog-modal-open');
    }

    function closeModal(modal) {
        modal.classList.remove('catalog-modal-overlay--visible');

        const anyOpen = document.querySelector('.catalog-modal-overlay.catalog-modal-overlay--visible');
        if (!anyOpen) {
            body.classList.remove('catalog-modal-open');
        }
    }

    // Открытие модалки по клику на карточку
    const catalogCards = document.querySelectorAll('.catalog-card');

    catalogCards.forEach(card => {
        card.addEventListener('click', function() {
            const productId = this.getAttribute('data-product-id');
            if (!productId) return;

            openModalById(productId);
        });
    });

    // Закрытие по крестику, кнопке "Закрыть" и клику по фону
    modalOverlays.forEach(overlay => {
        // Клик по фону
        overlay.addEventListener('click', function(e) {
            if (e.target === overlay) {
                closeModal(overlay);
            }
        });

        // Кнопки закрытия внутри модалки
        const closeButtons = overlay.querySelectorAll('[data-modal-close]');
        closeButtons.forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                closeModal(overlay);
            });
        });
    });

    // GSAP анимации для карточек (если GSAP подключен)
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        const catalogCards = document.querySelectorAll('.catalog-card');
        
        catalogCards.forEach((card, index) => {
            gsap.fromTo(card, 
                { 
                    opacity: 0, 
                    y: 30 
                },
                {
                    opacity: 1,
                    y: 0,
                    duration: 0.6,
                    delay: index * 0.1,
                    scrollTrigger: {
                        trigger: card,
                        start: 'top 85%',
                        toggleActions: 'play none none none'
                    }
                }
            );
        });
    }
});


