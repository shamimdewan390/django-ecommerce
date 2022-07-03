from django.shortcuts import render
from .models import *

# Create your views here.


def store(request):
    categories = Category.objects.all()[:4]
    products = Product.objects.all()
    context = {'categories': categories, 'products': products}
    return render(request, 'store/store.html', context)


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/products.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)


def product_view(request, pk):
    product = Product.objects.prefetch_related('color').prefetch_related('size').get(id=pk)
    context = {'product': product}
    return render(request, 'store/product-view.html',context)
