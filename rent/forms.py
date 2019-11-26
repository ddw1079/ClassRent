from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post, Comment, Building


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required. inform a valid email address.')

    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'email', 'password1', 'password2',}


class ChooseRoomForm(forms.ModelForm):

    class MetaL:
        building = forms.ModelChoiceField(queryset=Building.objects.all())

        model = Building
        fields = {'building', 'floor', 'room'}

        widget = {
            'building': forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'building_selector'}),
            'floor': forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'building_selector'}),
            'room': forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'building_selector'})
        }
