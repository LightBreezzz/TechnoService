from django import forms
from .models import audit_log
from django.core.validators import EmailValidator, RegexValidator

class audit_log_form(forms.ModelForm):
    email = forms.EmailField(
        validators=[EmailValidator(message="Invalid email address")]
        )

    phone = forms.CharField(
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')]
        )
    
    class Meta:
        model = audit_log
        fields = ['name', 'company', 'email', 'phone', 'service', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'service': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

