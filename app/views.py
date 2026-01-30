from django.shortcuts import render


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


def contacts(request):
    return render(request, 'app/contacts.html')