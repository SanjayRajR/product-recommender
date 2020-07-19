from django.db import models
from datetime import datetime
# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateField(default=datetime.now, blank=True)
    def __str(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(default="none",max_length=254)
    city = models.CharField(default="India",max_length=200)
    state = models.CharField(default="None",max_length=200)
    partnered_on = models.DateField(default=datetime.now, blank=True)
    description = models.TextField(blank=True)
    delivery_in = models.CharField(default="10days",max_length=30)
    
    def __str__(self):
        return self.name