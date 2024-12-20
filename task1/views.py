from django.shortcuts import render
from .models import *
from django.http import HttpResponse



def sing_in(requests):
    buyer = Buyer.objects.all()
    info = {}
    if requests.method == "POST":
        username = requests.POST.get("username")
        password = requests.POST.get("password")
        repeat_password = requests.POST.get("repeat_password")
        age = requests.POST.get("age")

        if password == repeat_password and int(age) >= 18 and username not in buyer:
            Buyer.objects.create(name=username, balance=2000, age=age)
            return HttpResponse(f'Приветсвуем на нашем сайте {username}!')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = "Вы должны быть старше 18"
        elif username in buyer:
            info['error'] = 'Имя пользователя уже занято'

    return render(requests, 'task1/registration_page.html', context=info)
# Create your views here.

