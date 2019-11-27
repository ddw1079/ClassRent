from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget

from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text', ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-100 form-control form-control-sm', 'placeholder': 'Title'}),
            'text': SummernoteWidget(),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'w-100 form-control form-control-sm', 'placeholder': 'author'}),
            'text': SummernoteWidget(),
        }


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required. inform a valid email address.')

    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'email', 'password1', 'password2', }


# class ChooseRoomForm(forms.ModelForm):
#
#     class Meta:
#         building = forms.ModelChoiceField(queryset=Building.objects.filter())
#         floor = forms.ModelChoiceField(queryset=Building.objects.all())
#         room = forms.ModelChoiceField(queryset=Building.objects.all())
#
#         model = Building
#         fields = {'building', 'floor', 'room'}
#
#         widgets = {
#             'building': forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'building_selector'}),
#             'floor': forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'floor_selector'}),
#             'room': forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'room_selector'})
#         }
