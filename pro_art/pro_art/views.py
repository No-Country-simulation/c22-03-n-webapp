from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Product, Category
from users.models import UserProfile

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    users = UserProfile.objects.all()
    context = {
        'categories': categories,
        'products': products,
        'users': UserProfile
    }
    return render(request, 'home.html', context)

