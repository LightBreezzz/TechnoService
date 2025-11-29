from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'app/index.html')


def print_outsourcing(request):
    return render(request, 'app/print_outsourcing.html')


def it_outsourcing(request):
    return render(request, 'app/it_outsourcing.html')


def software_solutions(request):
    return render(request, 'app/software_solutions.html')