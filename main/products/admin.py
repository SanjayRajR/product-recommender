from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_available', 'price', 'list_date', 'brand')
    list_display_links = ('id', 'name')
    list_filter = ('brand',)
    list_editable = ('is_available',)
    search_fields = ('name', 'description', 'type')
    list_per_page = 25


admin.site.register(Product, ProductAdmin)