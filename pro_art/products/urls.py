from django.urls import path
from products.views import Product_listView, Product_createView

urlpatterns = [
    path('listado/', Product_listView.as_view(), name='product_list'),
    path('registro/', Product_createView.as_view(), name='prduct_add')
]