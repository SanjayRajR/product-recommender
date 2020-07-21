from django.db import models
from datetime import datetime
from realtors.models import Seller
from django.contrib.auth.models import User
from django_mysql.models import ListTextField

product_category = {
    ('Smartphone', 'Smartphone'),
    ('Laptops', 'Laptops'),
    ('Earphones', 'Earphones'),
    ('Accessories', 'Accessories'),
}

brand_name = {
    ('Samsung', 'Samsung'),
    ('Apple', 'Apple'),
    ('Oneplus', 'Oneplus'),
    ('Dell', 'Dell'),
    ('HP', 'HP'),
    ('Lenovo', 'Lenovo'),
    ('jbl', 'jbl'),
    ('bose', 'bose'),
}

class Product(models.Model):
    seller = models.ForeignKey(Seller , on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, choices=brand_name)
    category = models.CharField(default="Accessories",max_length=200, choices=product_category)
    image = models.ImageField(upload_to='photos/%y/%m/%d/')
    image_1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    image_2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now,blank=True)
    specification = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    products = ListTextField(base_field=models.IntegerField(), size=10, blank=True)
    quantity = ListTextField(base_field=models.IntegerField(), size=10, blank=True)
    amount = ListTextField(base_field=models.IntegerField(), size=11, blank=True)
    list_date = models.DateField(auto_now_add=True)

