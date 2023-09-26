from django.shortcuts import render,  HttpResponse, redirect
from .models import Comment, CommentLike, Post
from .forms import PostForm
# Create your views here.


def get_home_page(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'portfolio4/home_page.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
        #Post.objects.create(author=current_user)
        return redirect('get_home_page')

    form = PostForm()
    context = {
        'form': form
    }

    return render(request, 'portfolio4/create_post.html', context)