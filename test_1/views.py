from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def test_1(request):
    return HttpResponse('test_1: hello world')


def test_2(request):
    return HttpResponse('test_2: hi!')


def index(request):
    return HttpResponse('<a href="https://google.com">go to google</a>')