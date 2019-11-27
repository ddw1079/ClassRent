from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import ListView
from django.views.generic.base import View

from .models import Post, Comment
from .forms import PostForm, CommentForm


# Create your views here.

class PostListView(ListView):
    template_name = "post_list.html"
    model = Post
    context_object_name = 'PostList'

    def get(self, request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

        # paginator (Page 기능)
        page = request.GET.get('page', 1)
        paginator = Paginator(posts, 20)
        max_index = len(paginator.page_range)
        current_page = int(page) if page else 1
        page_numbers_range = 5  # Display only 5 page numbers

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]

        try:
            content = paginator.page(page)
        except PageNotAnInteger:
            content = paginator.page(1)
        except EmptyPage:
            content = paginator.page(paginator.num_pages)

        return render(request, 'post_list.html', {'posts': content, 'page_range': page_range})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'post_draft_list.html', {'posts': posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post')


def registering(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
        else:
            form = UserCreationForm()
        return render(request, 'register.html', {'form': form})


def rent(request):
    return render(request, 'rentClass.html')


def about(request):
    return render(request, 'about.html')


def choose_room(request):
    return render(request, 'choose_room.html')


def check_reservation(request):
    return render(request, 'check_reservation.html')


# class ChooseRoom(View):
#     model = Building
#     form_class = ChooseRoomForm
#     template_name = 'choose_room.html'
#
#     def get(self, request):
#         context = self.get_context()
#         return render(request, 'choose_room.html', context)
#
#     def get_context(self):
#         self.context = {}
#         building = Building.objects.all()
#
#         self.context['building'] = building
#         return self.context
