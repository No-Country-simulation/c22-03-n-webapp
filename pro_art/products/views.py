from django.shortcuts import render
from django.urls import reverse_lazy
from products.forms import ProductForm
from .models import *
from django.views.generic import ListView, CreateView

# Vistas de productos
def product_list(request):
    data = {
        'title': 'Listado de productos',
        'products': Product.objects.prefetch_related("categories","images").all()
    }
    return render(request, "/list.html", data)


class Product_listView(ListView):
    model = Product
    template_name = 'products/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de productos'
        return context

class Product_createView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_create.html'
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de productos'
        return context
    

# # Listar todos los productos
# def product_list(request):
#     products = Product.objects.prefetch_related("categories","images").all()
#     context = {
#         'products': products
#     }
#     return render(request, "templates/list.html")


# # Detalle de un producto
# def product_detail(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     context = {
#         'product': product
#     }
#     return render(request, "templates/detail.html", context)

# # Resgistro de productos
# def product_create(request):
#     if request.method == 'POST':
#         product_form = ProductForm(request.POST, request.FILES)
#         if product_form.is_valid():
#             # Se guarda el producto
#             product  = product_form.save()
            
#             image = product_form.cleaned_data.get('image')
#             ProductImage.objects.create(product=product, image=image)
            
#             return redirect('productdetail')
    
#     else:
#         product_form = ProductForm()
    
#     context={
#         'form': product_form,
#         'title': 'Registro de productos'
#     }
    
#     return render(request, 'templates/create.html', context)