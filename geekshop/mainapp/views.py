import json
import os

from django.shortcuts import render
from django.conf import settings
from mainapp.models import Product, ProductCategory


def main(request):
    title = 'главная'
    products = Product.objects.all()[:4]
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    title = 'продукты'

    same_products = Product.objects.all()[:4]

    links_menu = ProductCategory.objects.all()
    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = 'о нас'
    locations = [
        {
            'city': 'Москва',
            'phone': '+7-888-888-8888',
            'email': 'info@stuls.ru',
            'address': 'Ул. Пушкина, д. Колотушкина'
        },
        {
            'city': 'Екатеринбург',
            'phone': '+7-777-777-7777',
            'email': 'info_yekaterinburg@stuls.ru',
            'address': 'Химмаш'
        },
        {
            'city': 'Владивосток',
            'phone': '+7-999-999-9999',
            'email': 'info_vladivistok@stuls.ru',
            'address': 'Прямо в порту'
        },
    ]

    content = {'title': title, 'locations': locations}
    return render(request, 'mainapp/contact.html', content)
