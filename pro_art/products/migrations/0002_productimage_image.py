# Generated by Django 4.2.16 on 2024-11-19 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='image',
            field=models.ImageField(null=True, upload_to=None),
        ),
    ]
