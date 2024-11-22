from django.urls import path, include
from django.views.generic import TemplateView

from .views import (
    OrderList,
)

urlpatterns = [

    path('orders/', OrderList.as_view(template_name="orders/index.html"),
         name='order_list'),
]
