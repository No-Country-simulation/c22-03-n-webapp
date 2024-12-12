from django.urls import path
from pro_art import settings
from products.views import *
from django.conf.urls.static import static



urlpatterns = [
    path('listado/', Product_listView.as_view(), name='product_list'),
    path('registro/', Product_createView.as_view(), name='product_add'),
    path('products/<int:pk>/', Product_detailView.as_view(), name='product_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)