from rest_framework import serializers
from .models import Product, Provider, Category


# Serializer para productos
class ProductSerializer(serializers.ModelSerializer):
    provider = serializers.StringRelatedField()  # Para mostrar el nombre del proveedor
    categories = serializers.StringRelatedField(many=True)  # Mostrar nombres de categorías
    provider_id = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all())
    categories_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all()
    )

    class Meta:
        model = Product
        fields = [
            'id',
            'provider',
            'provider_id',
            'categories',
            'categories_ids',
            'name',
            'quantities',
            'price_product',
            'description_product',
            'status',
        ]
