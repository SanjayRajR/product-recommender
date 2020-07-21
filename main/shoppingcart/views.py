from django.shortcuts import render, redirect
from products.models import Product, Order
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
import numpy as np
from django.contrib.auth.models import User
from django.contrib import messages 

@login_required(login_url="/accounts/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def cart_detail(request):
    return render(request, 'shoppingcart/cart_display.html')

@login_required(login_url="/accounts/login")
def cart_checkout(request):
    cart = Cart(request)
    if(cart.cart):
        quantity = []
        amount = []
        purchased_products = []

        for i in cart.cart:
            print(i, cart.cart[i]['quantity'], cart.cart[i]['price'])
            purchased_products.append(i)
            quantity.append(cart.cart[i]['quantity'])
            amount.append(int(cart.cart[i]['price']))

        amount = [amount[i] * quantity[i] for i in range(len(amount))]
        amount.append(sum(amount))
        quantity = [str(i) for i in quantity]
        amount = [str(i) for i in amount]
        order = Order(user=User.objects.get(id=request.user.id), products=purchased_products, quantity=quantity, amount=amount)
        order.save()
        cart.clear()

    else:
        messages.danger(request,'Cart is empty')
        return redirect('cart_detail')

    return redirect("index")
