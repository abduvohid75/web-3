from django.shortcuts import render

from main.models import Product


# Create your views here.

def index(request):
    product_list = Product.objects.all()

    context = {
        'object_list' : product_list,
        'title' : 'Главная'
    }

    return render(request, 'main/index.html', context)

def contacts(request):
    if (request.method == 'POST'):

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f'Имя: {name} Email: {email} Сообщение: {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'main/contacts.html', context)