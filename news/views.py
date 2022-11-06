from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from news.models import News


def get_message(request):
    return HttpResponse('<h1>Hello world message</h1><a href="/">back</a>')


def add_news(req):
    for i in range(10):
        News.objects.create(title=f'Новость {i+1}', content=f'Содержание новости {i+1}')
    return HttpResponse('ok')


def index(request):
    news = News.objects.all()
    contex = {
        'title': 'Список новостей',
        'news': news
    }
    return render(request, template_name='index.html', context=contex)