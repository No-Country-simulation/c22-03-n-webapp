from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Product, Category

def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'home.html', context)

