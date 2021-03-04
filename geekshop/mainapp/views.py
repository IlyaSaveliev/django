from django.shortcuts import render

def main(request):
    content = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', content)

def products(request):
    links_menu = [
        {'href': 'product_all', 'name': 'все'},
        {'href': 'product_home', 'name': 'дом'},
        {'href': 'product_office', 'name': 'офис'},
        {'href': 'product_modern', 'name': 'модерн'},
        {'href': 'product_classic', 'name': 'классика'},
    ]
    content = {
        'title': 'Продукты',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', content)

def contact(request):
    content = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', content)
