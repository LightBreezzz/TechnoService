from django.db import models
from django.conf import settings

class audit_log(models.Model):
    name = models.CharField("Имя", max_length=255, null=True, blank=True)
    company = models.CharField("Компания", max_length=255, null=True, blank=True)
    email = models.EmailField("Email", max_length=255, validators=[EmailValidator(message="Invalid email address")])
    phone = models.CharField("Телефон", max_length=10, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')])
    service = models.CharField("Услуга", max_length=255)
    message = models.TextField("Сообщение", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Create your models here.
