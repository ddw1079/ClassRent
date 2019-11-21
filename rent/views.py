from django.shortcuts import render

# Create your views here.


def rent(request):
    return render(request, 'rentClass.html')


def base(request):
    return render(request, 'base.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
