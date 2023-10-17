from django import forms
from .models import Post, Comment, ExtendedUser
from django.contrib.auth.forms import UserChangeForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['heading', 'content', 'categories', 'image']

class CommentForm(forms.ModelForm):
    #content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ['content', 'image']


class ProfilePictureForm(forms.ModelForm):
    
    class Meta:
        model = ExtendedUser
        fields = ['profileImage',]
