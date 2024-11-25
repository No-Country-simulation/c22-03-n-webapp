from django.urls import path, include
from django.views.generic import TemplateView

from .views import (
    OrderListView,
    OrderDetailView
)

urlpatterns = [

    path('orders/', OrderListView.as_view(template_name="orders/index.html"),
         name='order_list'),
    path('orders/detail/<int:pk>', OrderDetailView.as_view(template_name="orders/detail.html"),
         name='order_detail'),
]
