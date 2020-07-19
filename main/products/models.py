from django.db import models
from datetime import datetime
from realtors.models import Seller, Realtor
from django.contrib.auth.models import User

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
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now,blank=True)
    specification = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    products = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    review_statement = models.CharField(max_length=255)
    review_sentiment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True)