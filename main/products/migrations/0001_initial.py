# Generated by Django 3.0.3 on 2020-07-18 15:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_statement', models.CharField(max_length=255)),
                ('review_sentiment', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(choices=[('bose', 'bose'), ('Oneplus', 'Oneplus'), ('jbl', 'jbl'), ('Samsung', 'Samsung'), ('HP', 'HP'), ('Apple', 'Apple'), ('Lenovo', 'Lenovo'), ('Dell', 'Dell')], max_length=200)),
                ('type', models.CharField(choices=[('Accessories', 'Accessories'), ('Earphones', 'Earphones'), ('Smartphone', 'Smartphone'), ('Laptops', 'Laptops')], max_length=200)),
                ('sub_type', models.CharField(choices=[('Electronics', 'Electronics')], max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('weight', models.DecimalField(blank=True, decimal_places=1, max_digits=8)),
                ('photo_main', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('is_available', models.BooleanField(default=True)),
                ('list_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Seller')),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathroom', models.DecimalField(decimal_places=1, max_digits=2)),
                ('garage', models.IntegerField(default=0)),
                ('sqft', models.IntegerField()),
                ('lot_size', models.DecimalField(decimal_places=1, max_digits=5)),
                ('photo_main', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor')),
            ],
        ),
    ]
