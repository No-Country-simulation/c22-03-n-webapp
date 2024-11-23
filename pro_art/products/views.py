from django.shortcuts import get_object_or_404, redirect, render
from products.forms import ProductForm
from .models import Product, ProductImage


# Vistas de productos

# Listar todos los productos
def product_list(request):
    products = Product.objects.prefetch_related("categories","images").all()
    context = {
        'products': products
    }
    return render(request, "products/list.html")


# Detalle de un producto
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }
    return render(request, "products/detail.html", context)

# Resgistro de productos
def product_create(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            # Se guarda el producto
            product  = product_form.save()
            
            image = product_form.cleaned_data.get('image')
            ProductImage.objects.create(product=product, image=image)
            
            return redirect('productdetail')
    
    else:
        product_form = ProductForm()
    
    context={
        'form': product_form,
        'title': 'Registro de productos'
    }
    
    return render(request, 'products/create.html', context)