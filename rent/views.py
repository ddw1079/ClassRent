from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def rent(request):
    return render(request, 'rentClass.html')


def base(request):
    return render(request, 'base.html')


def login(request):
    return render(request, 'login.html', {})


def register(request):
    return render(request, 'register.html')
