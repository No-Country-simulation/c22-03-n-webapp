from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from users.models import Customer
from .models import Order, Payment, OrderDetail
from .forms import OrderDetailUpdateQuantityForm


class OrderListView(ListView):
    model = Order
    # TODO
    # debe de estar logueado

    def get_queryset(self):
        queryset = super().get_queryset()
        # TODO
        # filtrar por usuario logueado
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # TODO
        # modificarlo por el usuario logueado
        context['customer'] = Customer.objects.first()
        return context


class OrderDetailView(DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = context['object'].total
        return context


class OrderPaymentView(SuccessMessageMixin, CreateView):
    model = Payment
    fields = ("order", )

    def get_form_kwargs(self):
        self.order_pk = self.kwargs.get('order_pk')

        kwargs = super().get_form_kwargs()
        kwargs['initial']['order'] = self.order_pk
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = Order.objects.get(pk=self.order_pk)
        context['order'] = order
        return context

    def get_success_url(self):
        success_message = 'Pay correct !'
        messages.success(self.request, (success_message))
        return reverse('order_list')


class OrderDetailDeleteView(SuccessMessageMixin, DeleteView):
    model = OrderDetail
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro
    def get_success_url(self):
        success_message = f'Product  {self.object.product.name} deleted!'
        messages.success(self.request, (success_message))
        return reverse('order_detail', kwargs={'pk': self.object.order.pk})


class OrderDetailUpdateView(SuccessMessageMixin, UpdateView):
    model = OrderDetail
    form_class = OrderDetailUpdateQuantityForm

    # Redireccionamos a la página principal luego de actualizar un registro
    def get_success_url(self):
        success_message = f'Product {self.object.product.name} updated'
        messages.success(self.request, (success_message))
        return reverse('order_detail', kwargs={'pk': self.object.order.pk})
