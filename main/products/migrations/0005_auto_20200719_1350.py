# Generated by Django 3.0.3 on 2020-07-19 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200719_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('Lenovo', 'Lenovo'), ('Oneplus', 'Oneplus'), ('bose', 'bose'), ('Dell', 'Dell'), ('Samsung', 'Samsung'), ('jbl', 'jbl'), ('Apple', 'Apple'), ('HP', 'HP')], max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Accessories', 'Accessories'), ('Laptops', 'Laptops'), ('Smartphone', 'Smartphone'), ('Earphones', 'Earphones')], default='Accessories', max_length=200),
        ),
    ]
