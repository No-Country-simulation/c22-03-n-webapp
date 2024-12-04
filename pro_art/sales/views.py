from django.views.generic.base import RedirectView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

        context['title'] = 'Listado de Pedidos'
        return context


class OrderDetailView(DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = context['object'].total
        context['title'] = 'Order Detail'
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
        context['title'] = 'Payment'
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


class AddProductToCart(RedirectView):
    """
    model = OrderDetail
    template_name = 'orders/detail.html'
    fields = '__all__'
    def get_success_url(self):
        success_message = f'Product {self.object.product.name} added'
        messages.success(self.request, (success_message))
        return reverse('order_detail', kwargs={'pk': self.object.order.pk})
    """

    def post(self, request, *args, **kwargs):
        order_pk = {'pk': self.object.order.pk}
        if kwargs.objects.filter().exists():

            # Obtener el ususario loguedo
            # TODO
            # Saber el usuario logueado
        customer = Users.objects.first()
        # Buscar un order pending
        order = Order.objects.filter(
            status="PENDING", customer=customer).first()
        # Si no existe lo creo
        if order is None:
            order = Order(customer=customer, status="PENDING")
            order.save()

        # Busco si el producto ya esta en el pedido
        line = OrderDetail.objects.filter(product="pk", order=order).first()
        # si el producto ya esta en el pedido, actualizo la cantidad
        if line:
            line.quantity += 1
        # Si no existe el pedido o no esta dentro del pedido el producto, lo añado(creo orderdetail)
        else:
            # TODO
            # Falta saber como obtener product y quantity
            line = OrderDetail(order=order, product=product, quantity=quantity)

        line.save()

        # me guardo en algun sitio el pk del pedido, porque lo necesito para hacer el redirect
        self.__myorder = order

        return self.get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        success_message = f'Product {self.object.product.name} updated'
        messages.success(self.request, (success_message))
        return reverse('order_detail', kwargs={'pk': self.__myorder.pk})
