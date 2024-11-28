from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from users.models import Customer
from products.models import Product
from .models import Order, Payment


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
        total = 0
        print('---', context)
        print('object reservada', object)
        for od in context['object'].order_details.all():
            total += od.quantity * od.product.price_product
        context['total'] = total
        print(context)
        return context


class OrderPaymentView(CreateView):
    model = Payment
    fields = "__all__"

    def get_form_kwargs(self):
        self.order_pk = self.kwargs.get('order_pk')
        return super().get_form_kwargs()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # tengo el pk
        print("----", self.order_pk)
        # coger la instancia
        order = Order.objects.get(pk=self.order_pk)
        # devolver la instancia al template
        context['order'] = order
        # en el template mostrar la información
        # en el template poner un formulario con un boton pagar
        # el formulario tendrá el order_pk, total, fecha, tax
        # al darle al botón se genera el pago
        # cuando se genere el pago redirigir al listado de orders
        print(context)
        print("kwargs", kwargs)
        # print("request", self.request.__dict__)
        return context
