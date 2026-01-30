from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import audit_log_form


def contacts(request):
    if request.method == 'POST':
        form = audit_log_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваша заявка успешно отправлена. Мы свяжемся с вами в ближайшее время.')
            return redirect(reverse('contacts') + '#audit-form')
    else:
        form = audit_log_form()
    return render(request, 'app/contacts.html', {'form': form})

# Create your views here.
def index(request):
    return render(request, 'app/index.html')


def services(request):
    return render(request, 'app/services.html')


def catalog(request):
    return render(request, 'app/catalog.html')
def catalog_printers(request):
    return render(request, 'app/catalog_printers.html')


def about(request):
    return render(request, 'app/about.html')


def cases(request):
    return render(request, 'app/cases.html')
