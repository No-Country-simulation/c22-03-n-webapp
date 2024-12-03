from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from products.forms import ProductForm
from .models import *
from django.views.generic import ListView, CreateView,DetailView

# Vistas de productos
def product_list(request):
    data = {
        'title': 'Listado de productos',
        'products': Product.objects.prefetch_related("categories","images").all()
    }
    return render(request, "/list.html", data)


class Product_listView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        # Recupera todos los productos con sus categorías e imágenes relacionadas
        return Product.objects.prefetch_related('categories', 'images').all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de productos'
        return context

class Product_detailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'
    
    # Detalle de un producto
    def product_detail(request, product_id):
        product = Product.objects.prefetch_related("categories", "images").get(id=product_id)
        context = {
            'product': product,
        }
        return render(request, "products/detail.html", context)


    
class Product_createView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('product_list')

    def post(self, request):
        # Obtenemos el formulario del producto
        form = self.get_form()
        images = request.FILES.getlist('images')  # Obtiene las imágenes del formulario
        
        if form.is_valid():
            # Guardamos el producto
            product = form.save()
            # Guardamos las imágenes asociadas
            for image_file in images:
                ProductImage.objects.create(product=product, image=image_file)
            return HttpResponseRedirect(self.success_url)
        
        # Si el formulario no es válido, devolvemos el formulario con errores
        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        # Configuramos el contexto para pasar el título
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