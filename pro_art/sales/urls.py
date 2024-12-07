from django.urls import path

from .views import (
    OrderListView,
    OrderDetailView,
    OrderPaymentView,
    OrderDetailDeleteView,
    OrderDetailUpdateView,
)


urlpatterns = [

    path('orders/', OrderListView.as_view(
        template_name="orders/index.html"),
        name='order_list'
    ),
    path('orders/detail/<int:pk>', OrderDetailView.as_view(
        template_name="orders/detail.html"),
        name='order_detail'
    ),
    path('orders/<int:order_pk>/payment', OrderPaymentView.as_view(
        template_name="orders/payment.html"),
        name='order_payment'
    ),
    path('order_details/delete/<int:pk>', OrderDetailDeleteView.as_view(
        template_name="orders/detail.html"),
        name='order_detail_delete'
    ),
    path('order_details/update/<int:pk>', OrderDetailUpdateView.as_view(
        template_name="orders/detail.html"),
        name='order_detail_update'
    ),
    path('orders/add_product/<int:product_pk>', OrderDetailUpdateView.as_view(
        template_name="orders/detail.html"),
        name='add_product_to_order'
    ),
]
