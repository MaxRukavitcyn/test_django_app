from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def get_message(request):
    return HttpResponse('<h1>Hello world message</h1><a href="/">back</a>')


def index(request):
    return render(request, 'index.html')