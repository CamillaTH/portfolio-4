from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['heading', 'content', 'categories', 'image']

class CommentForm(forms.ModelForm):
    #content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ['content', 'image']
