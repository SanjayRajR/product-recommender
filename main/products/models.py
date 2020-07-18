from django.db import models
from datetime import datetime
from realtors.models import Seller, Realtor
from django.contrib.auth.models import User


# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathroom = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now,blank=True)
    def __str__(self):
        return self.title


PRODUCT_TYPE = {
    ('Fruites_Vegitables', 'Fruites_Vegitables'),
    ('Food_Drinks', 'Food_Drinks'),
}

product_sub_type = {
    ('veg', 'veg'),
    ('Non_veg', 'Non_veg'),
    ('Cooking', 'Cooking'),
    ('Ready_Food', 'Ready_Food'),
}
brand_name = {
    ('MTR', 'MTR'),
    ('Dairy_Milk', 'Dairy_Milk'),
    ('Nandini', 'Nandini'),
    ('Nescafe', 'Nescafe'),
    ('Sunset', 'Sunset'),
    ('KFC', 'KFC'),
    ('Pepsi', 'Pepsi'),
    ('Sea_Cone', 'Sea_Cone'),
}

class Product(models.Model):
    seller = models.ForeignKey(Seller , on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, choices=brand_name)
    type = models.CharField(max_length=200, choices=PRODUCT_TYPE)
    sub_type = models.CharField(max_length=100, choices=product_sub_type)
    #zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    weight = models.DecimalField(max_digits=8, decimal_places=1,blank=True)
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    is_available = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now,blank=True)
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