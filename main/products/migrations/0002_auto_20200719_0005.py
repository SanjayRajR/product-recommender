# Generated by Django 3.0.3 on 2020-07-18 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('Dell', 'Dell'), ('Lenovo', 'Lenovo'), ('Oneplus', 'Oneplus'), ('Samsung', 'Samsung'), ('jbl', 'jbl'), ('bose', 'bose'), ('Apple', 'Apple'), ('HP', 'HP')], max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Accessories', 'Accessories'), ('Smartphone', 'Smartphone'), ('Earphones', 'Earphones'), ('Laptops', 'Laptops')], max_length=200),
        ),
    ]
