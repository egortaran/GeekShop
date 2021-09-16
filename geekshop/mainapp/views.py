import random

from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mainapp.models import Product, ProductCategory


def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.filter()
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.filter()


def get_same_products(hot_product):
    same_products = Product.objects.filter(is_active=True).select_related('category').exclude(pk=hot_product.pk).filter(category = hot_product.category)
    return same_products


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product_{pk}'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Product, pk=pk)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Product, pk=pk)


def get_products():
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True).select_related('category')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True).select_related('category')


def get_hot_product():
    products = get_products()

    return random.sample(list(products), 1)[0]


def get_products_orederd_by_price():
    if settings.LOW_CACHE:
        key = 'products_orederd_by_price'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True).order_by('price')


def products(request, pk=None, page=1):
    title = 'продукты/каталог'

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    links_menu = get_links_menu()
    products = get_products_orederd_by_price()

    if pk is not None:
        if pk == 0:
            products = products
            category = {'pk': 0, 'name': 'все'}

            product = random.sample(list(products), 1)[0]
            same_products = get_same_products(product)

            paginator = Paginator(products, 1)
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(is_active=True, category__pk=pk).order_by('price')

            product = random.sample(list(products), 1)[0]
            same_products = get_same_products(product)

            paginator = Paginator(products, 1)
            products = products[:2]

        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context = {
            'title': title,
            'links_menu': links_menu,
            'hot_product': hot_product,
            'same_products': same_products,
            'products': products,
            'products_paginator': products_paginator,
            'category': category,
        }
        return render(request=request, template_name='mainapp/products.html', context=context)

    context = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
        'products': products,
    }
    return render(request=request, template_name='mainapp/products.html', context=context)


def product(request, pk):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    product = get_object_or_404(Product, pk=pk)

    same_products = get_same_products(product)
    context = {
        'title': title,
        'links_menu': links_menu,
        'related_products': same_products,
        'product': product,
    }
    return render(request, 'mainapp/product.html', context)