from django.shortcuts import render,  HttpResponse, redirect
from .models import  Post, Comment #, CommentLike,
from .forms import PostForm
from django.views import generic
# Create your views here.


def get_index_page(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
        #Post.objects.create(author=current_user)
        return redirect('get_index_page')

    form = PostForm()
    context = {
        'form': form
    }

    return render(request, 'create_post.html', context)
