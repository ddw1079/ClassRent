from django.shortcuts import render
from rent.models import Post

# Create your views here.


def post_list(request):
    return render(request,'post_list.html')


def rent(request):
    return render(request, 'rentClass.html')


def base(request):
    return render(request, 'base.html')


def login(request):
    return render(request, 'login.html', {})


def register(request):
    return render(request, 'register.html')
