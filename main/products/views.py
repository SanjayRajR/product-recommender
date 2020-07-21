from django.shortcuts import render,redirect,get_object_or_404
from .models import Product, Order
from realtors.models import Seller
from shoppingcart.views import cart_add
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
import json
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from mlxtend.frequent_patterns import apriori
import numpy as np
import pandas as pd
import time
from mlxtend.preprocessing import TransactionEncoder
from products.choices import price_choices,type_choices,brand_choices
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.pipeline import Pipeline



def index(request):
    products = Product.objects.order_by('-list_date').filter(is_available=True)

    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'products': paged_listings,
        'type_choices': type_choices,
        'brand_choices': brand_choices,
        'values': request.GET
    }
    return render(request, 'products/view_products.html',context)

def product(request, product_id):
    cart_add(request, product_id)
    product = get_object_or_404(Product, pk=product_id)
    transaction = Order.objects.values_list('products')
    transaction_ids = [list(x) for x in transaction]
    num = []
    for row in transaction_ids:
        for ids in row:
            listToStr = ' '.join([str(x) for x in ids]) 
            list_of_ids = listToStr.split(' ')
            num.append([int(x) for x in list_of_ids])
    pro = product_id
    sub_dataset = []
    for i in num:
        if pro in i:
            sub_dataset.append(i)
    te = TransactionEncoder()
    te_ary = te.fit(sub_dataset).transform(sub_dataset)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    df1 = df
    df1[pro] = False
    df2 = apriori(df1, min_support=0.01, use_colnames=True)
    df2 = df2.sort_values(by='support', ascending=False)
    list1 = np.array(df2['itemsets'])
    newlol = []
    for i in df2['itemsets']:
        newlol.append(list(i))
    newlol = newlol[0]
    suggested_product = Product.objects.get(id=int(newlol[0]))
    seller = Seller.objects.get(name=product.seller)
    print(suggested_product)
    context = {
        'product': product,
        'product_id':product_id,
        'user': request.user,
        'seller':seller,
        'suggested_product': suggested_product
    }
    print(context)
    time.sleep(1)
    return render(request, 'products/product.html',context)

def search(request):
    queryset_list = Product.objects.order_by('-list_date')

    # Category Search
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(category__iexact=category)

    # Brand Search
    if 'brand' in request.GET:
        brand = request.GET['brand']
        if brand:
            queryset_list = queryset_list.filter(brand__iexact=brand)


    if 'search' in request.GET:
        search = request.GET['search']
        if search:
            queryset_list = queryset_list.filter(specification__icontains=search)

    # Price Search
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'products': queryset_list,
        'price_choices': price_choices,
        'brand_choices': brand_choices,
        'type_choices': type_choices,
        'values': request.GET
    }
    return render(request, 'products/search.html',context)

