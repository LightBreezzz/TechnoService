from django import forms
from .models import audit_log
from django.core.validators import EmailValidator, RegexValidator


class audit_log_form(forms.ModelForm):
    email = forms.EmailField(
        validators=[EmailValidator(message="Введите корректный email")],
        required=True,
    )
    phone = forms.CharField(
        validators=[RegexValidator(regex=r'^[\d\s\+\-\(\)]{10,25}$', message="Введите корректный номер (от 10 цифр)")],
        required=True,
    )

    class Meta:
        model = audit_log
        fields = ['name', 'company', 'email', 'phone', 'service', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'contacts-form__input', 'placeholder': 'Введите ваше имя'}),
            'company': forms.TextInput(attrs={'class': 'contacts-form__input', 'placeholder': 'Название компании'}),
            'email': forms.EmailInput(attrs={'class': 'contacts-form__input', 'placeholder': 'Ваш email'}),
            'phone': forms.TextInput(attrs={'class': 'contacts-form__input', 'placeholder': '+7 (___) ___-__-__', 'type': 'tel'}),
            'service': forms.TextInput(attrs={'class': 'contacts-form__input', 'placeholder': 'Например, IT-аутсорсинг'}),
            'message': forms.Textarea(attrs={'class': 'contacts-form__textarea', 'placeholder': 'Опишите вашу ситуацию или задачу'}),
        }

