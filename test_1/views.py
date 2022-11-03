from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from test_1.models import Car


def get_message(request):
    return HttpResponse('<h1>Hello world message</h1><a href="/test_1">back</a>')


def index(request):
    return render(request, 'index.html')