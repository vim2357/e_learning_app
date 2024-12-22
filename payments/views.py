from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Payment

# Список всех платежей
class PaymentListView(ListView):
    model = Payment
    template_name = 'payments/payment_list.html'  # Путь к шаблону
    context_object_name = 'payments'  # Имя переменной в шаблоне

# Детали одного платежа
class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'payments/payment_detail.html'  # Путь к шаблону
    context_object_name = 'payment'  # Имя переменной в шаблоне
