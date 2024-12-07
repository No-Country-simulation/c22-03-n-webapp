from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Product, Category

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'home.html', context)

