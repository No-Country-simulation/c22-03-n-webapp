from django import forms
from .models import Product, ProductImage

class ProductForm(forms.ModelForm):
    images = forms.ImageField(required=True, label="Imagen del producto")
    
    class Meta:
        model = Product
        fields = [
            'name',
            'quantities',
            'price_product',
            'description_product',
            'status',
            'categories',
            'images'
        ]
        widgets = {
            'categories': forms.CheckboxSelectMultiple()
        }

# class ProductImageForm(forms.ModelForm):
#     class Meta:
#         model = ProductImage
#         fields = ['image']