from typing import Any
from django.views.generic.base import RedirectView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Order, Payment, OrderDetail
from .forms import OrderDetailUpdateQuantityForm
from products.models import Product
from users.models import UserProfile


class OrderListView(ListView):
    model = Order
    ordering = ['-pk']
    # TODO
    # debe de estar logueado

    def get_queryset(self):
        queryset = super().get_queryset()
        # TODO
        # filtrar por usuario logueado
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Listado de Pedidos'
        return context


class OrderDetailView(DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = context['object'].total
        context['title'] = 'Detalles del pedido'
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
        context['title'] = 'Pagos'
        return context

    def get_success_url(self):
        success_message = 'Pagado correctamente !'
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
        success_message = f'Producto {self.object.product.name} actualizado'
        messages.success(self.request, (success_message))
        return reverse('order_detail', kwargs={'pk': self.object.order.pk})


class AddProductToCart(RedirectView):
    def post(self, request, *args, **kwargs):
        # Obtener el ususario loguedo
        if not request.user.is_authenticated:
            self.__redirect_to = "login"
            return super().get(request, *args, **kwargs)
        # TODO
        # como relacionar usuario (Django) logueado con Users (pro_art)
        customer = UserProfile.objects.first()

        product_pk = kwargs['pk']
        product = Product.objects.filter(pk=product_pk).first()
        if not product:
            self.__redirect_to = "inicio"
            return super().get(request, *args, **kwargs)

        # Buscar un order pending
        order = Order.objects.filter(
            status="PENDING", customer=customer).first()
        # Si no existe lo creo
        if order is None:
            order = Order(customer=customer, status="PENDING")
            order.save()

        # Busco si el producto ya esta en el pedido
        line = OrderDetail.objects.filter(product=product, order=order).first()
        if line:
            # si el producto ya esta en el pedido, actualizo la cantidad
            line.quantity += 1
        else:
            # Si no existe el pedido o no esta dentro del pedido el producto, lo añado(creo orderdetail)
            line = OrderDetail(order=order, product=product, quantity=1)

        # guardo los cambios de la linea de pedido
        line.save()

        # me guardo en algun sitio el pk del pedido, porque lo necesito para hacer el redirect
        self.__redirect_to = "order_detail"
        self.__myorder = order
        self.__product = product

        return self.get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        if self.__redirect_to == "order_detail":
            success_message = f'Producto {self.__product.name} añadido al carrito'
            kwargs = {'pk': self.__myorder.pk}
        elif self.__redirect_to == "inicio":
            success_message = 'Producto no encontrado'
            kwargs = {}
        else:
            success_message = 'Debes de estar logueado'
            kwargs = {}
        messages.success(self.request, (success_message))
        return reverse(self.__redirect_to, kwargs=kwargs)
