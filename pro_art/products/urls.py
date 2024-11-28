from django.urls import path
from products.views import *

urlpatterns = [
    path('listado/', Product_listView.as_view(), name='product_list'),
    path('registro/', Product_createView.as_view(), name='product_add'),
    path('products/<int:pk>/', Product_detailView.as_view(), name='product_detail')
]