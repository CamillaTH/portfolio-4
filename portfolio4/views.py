from django.shortcuts import render,  HttpResponse
from .models import Comment, CommentLike, Post
# Create your views here.


def get_home_page(request):
    posts = Comment.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'portfolio4/home_page.html', context)
