# Generated by Django 4.2.16 on 2024-12-12 22:25
from django.db import migrations

def create_default_categories(apps, schema_editor):
    Category = apps.get_model('products', 'Category')
    default_categories = [
        'Joyería Artesanal',
        'Decoración para el Hogar',
        'Textiles',
        'Cerámica y Alfarería',
        'Productos de Madera',
        'Cosmética Natural',
        'Accesorios'
    ]
    for category_name in default_categories:
        Category.objects.create(name=category_name)

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_categories),
    ]