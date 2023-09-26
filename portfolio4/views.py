from django.shortcuts import render,  HttpResponse, redirect
from .models import Comment, CommentLike, Post
# Create your views here.


def get_home_page(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'portfolio4/home_page.html', context)

def create_post(request):
    if request.method == 'POST':
        current_user = request.user
        heading = request.POST.get('post_heading')
        content = request.POST.get('post_content')
        Post.objects.create(author=current_user, heading=heading, content=content)

        return redirect('get_home_page')
    return render(request, 'portfolio4/create_post.html')