from django import forms
from .models import Post, Comment, ExtendedUser
from django.contrib.auth.forms import UserChangeForm


class PostForm(forms.ModelForm):
    '''form for post a post'''
    class Meta:
        model = Post
        fields = ['heading', 'content', 'categories', 'image']

class CommentForm(forms.ModelForm):
    '''form for comment'''

    class Meta:
        model = Comment
        fields = ['content', 'image']


class ProfilePictureForm(forms.ModelForm):
    '''Form for profile picture'''
    class Meta:
        model = ExtendedUser
        fields = ['profileImage',]
