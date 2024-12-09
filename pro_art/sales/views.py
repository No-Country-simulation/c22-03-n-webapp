from django.http import Http404
from django.views.generic.base import RedirectView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Order, Payment, OrderDetail
from .forms import OrderDetailUpdateQuantityForm
from products.models import Product
from django.shortcuts import redirect


class OrderViewAbstract(object):

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)


class OrderListView(OrderViewAbstract, ListView):
    model = Order
    ordering = ['-pk']

    def get_queryset(self):
        queryset = super().get_queryset().filter(customer=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Pedidos'
        return context


class OrderDetailView(OrderViewAbstract, DetailView):
    model = Order

    def get_queryset(self):
        queryset = super().get_queryset().filter(customer=self.request.user)
        return queryset

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            return redirect("/")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = context['object'].total
        context['title'] = 'Detalles del pedido'
        return context


class OrderPaymentView(OrderViewAbstract, SuccessMessageMixin, CreateView):
    model = Payment
    fields = ("order", )

    def dispatch(self, request, *args, **kwargs):
        result = super().dispatch(request, *args, **kwargs)

        self.order_pk = self.kwargs.get('order_pk')
        order = Order.objects.filter(
            pk=self.order_pk,
            customer=self.request.user
        ).first()
        if not order:
            return redirect("/")
        return result

    def get_form_kwargs(self):
        self.order_pk = self.kwargs.get('order_pk')

        kwargs = super().get_form_kwargs()
        kwargs['initial']['order'] = self.order_pk
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = Order.objects.filter(pk=self.order_pk).first()
        if order:
            context['order'] = order

        context['order'] = order
        context['title'] = 'Pagos'
        return context

    def get_success_url(self):
        success_message = 'Pagado correctamente !'
        messages.success(self.request, (success_message))
        return reverse('order_list')


class OrderDetailDeleteView(
    OrderViewAbstract, SuccessMessageMixin, DeleteView
):
    model = OrderDetail
    fields = "__all__"

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            order__customer=self.request.user
        )
        return queryset

    # Redireccionamos a la página principal luego de eliminar un registro
    def get_success_url(self):
        success_message = f'Producto  {self.object.product.name} borrado del carrito'  # noqa
        messages.success(self.request, (success_message))
        return reverse('order_detail', kwargs={'pk': self.object.order.pk})


class OrderDetailUpdateView(
    OrderViewAbstract, SuccessMessageMixin, UpdateView
):
    model = OrderDetail
    form_class = OrderDetailUpdateQuantityForm

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            order__customer=self.request.user
        )
        return queryset

    # Redireccionamos a la página principal luego de actualizar un registro
    def get_success_url(self):
        success_message = f'Producto {self.object.product.name} actualizado'
        messages.success(self.request, (success_message))
        return reverse('order_detail', kwargs={'pk': self.object.order.pk})


class AddProductToCart(RedirectView):
    def post(self, request, *args, **kwargs):
        # Obtener el ususario loguedo
        if not request.user.is_authenticated or self.request.user.is_anonymous:
            return redirect("/")

        customer = self.request.user
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
            # Si no existe el pedido o no esta dentro del pedido el producto,
            # lo añado(creo orderdetail)
            line = OrderDetail(order=order, product=product, quantity=1)

        # guardo los cambios de la linea de pedido
        line.save()

        # me guardo en algun sitio el pk del pedido,
        # porque lo necesito para hacer el redirect
        self.__redirect_to = "order_detail"
        self.__myorder = order
        self.__product = product

        return self.get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        if self.__redirect_to == "order_detail":
            success_message = f'Producto {self.__product.name} añadido al carrito'  # noqa
            kwargs = {'pk': self.__myorder.pk}
        elif self.__redirect_to == "inicio":
            success_message = 'Producto no encontrado'
            kwargs = {}
        else:
            success_message = 'Debes de estar logueado'
            kwargs = {}
        messages.success(self.request, (success_message))
        return reverse(self.__redirect_to, kwargs=kwargs)
