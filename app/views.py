from django.shortcuts import render
from .forms import audit_log_form
from .models import audit_log
from django.shortcuts import redirect


def audit_log_view(request):
    if request.method == 'POST':
        form = audit_log_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts')
    else:
        form = audit_log_form()
    return render(request, 'app/contacts.html', {'form': form})

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def contacts(request):
    return render(request, 'app/contacts.html')