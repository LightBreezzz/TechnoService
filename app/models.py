from django.db import models
from django.core.validators import (
    RegexValidator, MinValueValidator, MaxValueValidator
)

# Create your models here.
class TechCategory(models.Model):
    """Офисная техника"""
    category_name = models.CharField(
        verbose_name="Название категории",
        primary_key=True,
        max_length=100
    )

    class Meta:
        verbose_name = "категорию техники"
        verbose_name_plural = "Категории техники"

    def __str__(self):
        return self.category_name


class Appliance(models.Model):
    """Конкретная модель техники"""
    appliance_name = models.CharField(
        verbose_name="Название товара",
        max_length=100
    )

    description = models.CharField(
        verbose_name="Описание",
        max_length=1000
    )

    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="products/",
        null=True,
        blank=True
    )

    category = models.ForeignKey(
        TechCategory, 
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name='tech_items'
    )

    """Здесь основные характеристики"""

    tech_type = models.CharField(
        verbose_name="Тип устройства",
        max_length=100,
        null=True,
        blank=True
    )

    print_type = models.CharField(
        verbose_name="Тип печати",
        max_length=100,
        null=True,
        blank=True
    )

    print_technique = models.CharField(
        verbose_name="Технология печати",
        max_length=100,
        null=True,
        blank=True
    )

    placement = models.CharField(
        verbose_name="Размещение",
        max_length=100,
        null=True,
        blank=True
    )

    productivity = models.CharField(
        verbose_name="Кол-во страниц в месяц",
        max_length=100,
        null=True,
        blank=True
    )

    double_print = models.CharField(
        verbose_name="Автоматическая двусторонняя печать",
        max_length=100,
        null=True,
        blank=True
    )

    print_resolution = models.CharField(
        verbose_name="Макс. разрешение печати",
        max_length=100,
        null=True,
        blank=True
    )

    print_speed = models.CharField(
        verbose_name="Скорость печати",
        max_length=100,
        null=True,
        blank=True
    )

    warm_up_time = models.CharField(
        verbose_name="Время разогрева",
        max_length=100,
        null=True,
        blank=True
    )

    first_print_time = models.CharField(
        verbose_name="Время первого отпечатка",
        max_length=100,
        null=True,
        blank=True
    )

    scanner_type = models.CharField(
        verbose_name="Тип сканера/реверс",
        max_length=100,
        null=True,
        blank=True
    )

    """Доп. поля"""

    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name="Дата обновления",
        auto_now=True
    )

    class Meta:
        verbose_name = "офисную технику"
        verbose_name_plural = "Офисная техника"

    def __str__(self):
        return self.appliance_name