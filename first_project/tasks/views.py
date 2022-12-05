from django.shortcuts import HttpResponse
from datetime import datetime


def greeting_(request):
    return HttpResponse("Hello : Welcome Django world")


def introduction_(request):
    text = "Django is a high-level Python web framework that enables rapid development of secure and maintainable websites."
    return HttpResponse(text)


def ddmmyy(request):
    return HttpResponse(f"{datetime.now().day}/{datetime.now().month}/{datetime.now().year}")


def square(request):
    dict_ = {}
    for i in range(1, 16):
        dict_[i] = i ** 2
    print(dict_)
    return HttpResponse(f"{dict_}")


from django.shortcuts import render

# Create your views here.
