from django.db import models
from django.conf import settings
from django.core.validators import EmailValidator, RegexValidator


# --- Подписки на услуги ---

class Subscription(models.Model):
    """Подписка на услугу."""
    name = models.CharField("Название", max_length=255)
    image = models.ImageField("Фото", upload_to="subscriptions/", blank=True, null=True)
    price = models.PositiveIntegerField("Стоимость (₽/мес)")
    description = models.TextField("Описание", blank=True)
    # Доп. информация
    type_label = models.CharField("Тип", max_length=255, default="Подписка на услугу", blank=True)
    payment_period = models.CharField("Период оплаты", max_length=100, default="Ежемесячно", blank=True)
    min_term = models.CharField("Минимальный срок", max_length=100, blank=True)
    support = models.CharField("Поддержка", max_length=255, blank=True)
    order = models.PositiveIntegerField("Порядок отображения", default=0)
    is_active = models.BooleanField("Активна", default=True)

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class SubscriptionFeature(models.Model):
    """Возможность подписки (строка в списке)."""
    subscription = models.ForeignKey(
        Subscription, on_delete=models.CASCADE, related_name="features", verbose_name="Подписка"
    )
    text = models.CharField("Текст", max_length=255)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Возможность подписки"
        verbose_name_plural = "Возможности подписки"
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.subscription.name}: {self.text[:50]}"


# --- Товары (принтеры, МФУ и т.д.) ---

class Product(models.Model):
    """Товар."""
    name = models.CharField("Название", max_length=255)
    image = models.ImageField("Фото", upload_to="products/", blank=True, null=True)
    price = models.PositiveIntegerField("Стоимость (₽)")
    description = models.TextField("Описание", blank=True)
    # Доп. информация
    type_label = models.CharField("Тип", max_length=255, blank=True)
    format_field = models.CharField("Формат", max_length=100, blank=True)
    warranty = models.CharField("Гарантия", max_length=100, blank=True)
    order = models.PositiveIntegerField("Порядок отображения", default=0)
    is_active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class ProductFeature(models.Model):
    """Возможность товара (строка в списке)."""
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="features", verbose_name="Товар"
    )
    text = models.CharField("Текст", max_length=255)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Возможность товара"
        verbose_name_plural = "Возможности товара"
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.product.name}: {self.text[:50]}"


# --- Прочее ---

class audit_log(models.Model):
    name = models.CharField("Имя", max_length=255, null=True, blank=True)
    company = models.CharField("Компания", max_length=255, null=True, blank=True)
    email = models.EmailField("Email", max_length=255, validators=[EmailValidator(message="Invalid email address")])
    phone = models.CharField("Телефон", max_length=25, validators=[RegexValidator(regex=r'^[\d\s\+\-\(\)]{10,25}$', message="Введите корректный номер телефона")])
    service = models.CharField("Услуга", max_length=255, blank=True)
    message = models.TextField("Сообщение", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Create your models here.
