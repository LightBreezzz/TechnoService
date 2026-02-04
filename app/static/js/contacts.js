// Базовая инициализация для страницы "Контакты" и формы заказа
document.addEventListener('DOMContentLoaded', function () {
    const contactsSection = document.querySelector('.contacts-main');
    if (contactsSection) {
        // Здесь в будущем можно добавить карту или отправку формы
        console.log('Страница "Контакты" загружена');
    }

    // Если мы на странице оформления заказа, передаём товары из localStorage в скрытое поле формы
    const orderItemsInput = document.querySelector('[data-order-cart-items]');
    if (orderItemsInput) {
        try {
            const raw = localStorage.getItem('ts_cart');
            orderItemsInput.value = raw || '[]';
        } catch (e) {
            orderItemsInput.value = '[]';
        }
    }
});

