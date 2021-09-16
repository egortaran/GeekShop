from django.shortcuts import render

from mainapp.models import ProductCategory, Product
from mainapp.views import get_hot_product, get_same_products


def index(request):
    title = 'магазин'

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    links_menu = ProductCategory.objects.all()
    products = Product.objects.all().order_by('price')

    context = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
        'slogan': 'супер предложения',
        'products': products,
    }
    title = 'магазин'

    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = 'контакты'
    context = {
        'title': title,
    }
    return render(request, 'geekshop/contact.html', context)