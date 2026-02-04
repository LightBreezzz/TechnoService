from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import audit_log_form, OrderForm
import json


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


def order(request):
    """
    Оформление заказа из корзины.
    Форма такая же, как для аудита, плюс сохраняем товары и сумму.
    """
    if request.method == "POST":
        form = OrderForm(request.POST)
        raw_items = request.POST.get("cart_items", "[]")
        try:
            items = json.loads(raw_items)
        except json.JSONDecodeError:
            items = []

        total = 0
        for item in items:
            try:
                price = int(item.get("price", 0))
                qty = int(item.get("qty", 0))
            except (TypeError, ValueError):
                price = 0
                qty = 0
            total += max(price, 0) * max(qty, 0)

        if form.is_valid() and items:
            order_obj = form.save(commit=False)
            order_obj.items = items
            order_obj.total_price = total
            order_obj.save()
            messages.success(
                request,
                "Ваш заказ успешно отправлен. Мы свяжемся с вами для уточнения деталей.",
            )
            # Показываем сообщение об успехе на странице оформления заказа
            return redirect("order")

        if not items:
            messages.error(request, "Корзина пуста. Добавьте товары и повторите попытку.")
    else:
        form = OrderForm()

    return render(request, "app/order.html", {"form": form})
