from django.shortcuts import render
from django.http import HttpResponse

from products.models import Product
from realtors.models import Seller
from products.choices import type_choices,brand_choices


# Create your views here.
def index(request):
    products = Product.objects.order_by('-list_date').filter(is_available=True)[:4]
    # shows 3 products on the index page based on the creation date

    context = {
        'products' : products,
        'brand_choices': brand_choices,
        'type_choices': type_choices,
    }
    return render(request,'home/index.html',context)

def about(request):
    realtors = Seller.objects.order_by('-contract_date')

    mvp_realtors = Seller.objects.all().filter(is_top=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'home/about.html',context)