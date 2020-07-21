from django.db import models
from datetime import datetime
# Create your models here.

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