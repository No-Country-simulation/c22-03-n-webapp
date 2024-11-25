from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from users.models import Customer
# from django.shortcuts import render
from .models import Order


class OrderListView(ListView):
    model = Order
    # debe de estar logueado

    def get_queryset(self):
        queryset = super().get_queryset()
        # filtrar por usuario logueado
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # modificarlo por el usuario logueado
        context['customer'] = Customer.objects.first()
        print(context)
        return context


class OrderDetailView(DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # modificarlo por el usuario logueado
        # context['customer'] = Customer.objects.first()
        print(context)
        return context


class PaymentTotal(CreateView):
