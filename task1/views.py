from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import News


def sing_in(request):
    buyer = Buyer.objects.all()
    info = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")

        if password == repeat_password and int(age) >= 18 and username not in str(buyer):
            Buyer.objects.create(name=username, balance=2000, age=age)
            return HttpResponse(f'Приветсвуем на нашем сайте {username}!')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = "Вы должны быть старше 18"
        elif username in str(buyer):
            info['error'] = 'Имя пользователя уже занято'

    return render(request, 'task1/registration_page.html', context=info)

def news(request):
    news_list = News.objects.all().order_by('-date')
    paginator = Paginator(news_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_obj': page_obj})



# Create your views here.

