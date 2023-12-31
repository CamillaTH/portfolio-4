from django.shortcuts import render,  HttpResponse, redirect, get_object_or_404
from .models import  Post, Comment, Category, ExtendedUser
from .forms import PostForm, CommentForm, ProfilePictureForm
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from allauth.account.forms import ChangePasswordForm, SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.utils.text import slugify
import datetime

# Create your views here.


def create_post(request):
    '''View for create post'''
    post_form = PostForm()

    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.author = request.user
            instance.image = request.FILES['image']

            # Generate a unique slug
            base_slug = slugify(instance.heading)
            unique_slug = base_slug
            count = 1

            while Post.objects.filter(slug=unique_slug).exists():
                # Slug already exists, append a count to make it unique
                count += 1
                unique_slug = f'{base_slug}-{count}'

            instance.slug = unique_slug
            instance.save()

            return redirect('create_post')

    return render(request, 'create_post.html', {'post_form': post_form})


class CategoryList(generic.ListView):
    '''view for listing categories'''
    model = Category
    queryset = Category.objects.order_by('name')
    template_name = 'base.html'
    paginate_by = 10

class PostList(generic.ListView):
    '''view to show post in list '''
    model = Post
    queryset = Post.objects.order_by('creation_time')
    template_name = 'base.html'
    paginate_by = 5

def Home_items(request):
       categories = Category.objects.all()
       posts = Post.objects.all()
       context = {
              'categories': categories,
              'posts': posts
       }
       return render(request, 'index.html', context)

class CategoryDetail(View):
    '''view to display category dettail Work in progress.... '''
    def get(self, request, slug, *args, **kwargs):
        queryset = Category.objects
        categories = get_object_or_404(queryset, slug=slug)

    pass

@login_required
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.user in post.likes.all():
        post.unlike_post(request.user)
    else:
        post.like_post(request.user)

    return redirect('post_detail', slug=slug)

def post_detail(request, slug):
    '''view for post detail and comment form'''
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved=True).order_by("-creation_time")
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            #Todo fix bug 
            #new_comment.image = request.FILES['image']
            new_comment.save()
            return redirect('post_detail', slug=slug)
    else:
        comment_form = CommentForm()

        
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'comment_form': CommentForm()})


@login_required
def like_comment(request, slug):
    comment = get_object_or_404(Comment, slug=slug)
    
    if request.user in comment.likes.all():
        comment.unlike_comment(request.user)
    else:
        comment.like_comment(request.user)

    return redirect('post_detail', slug=comment.post.slug)

def handler404(request, exception):
    '''handles 404 page'''

    return render(request, '404.html', status=404)


@login_required
def profile(request):
    '''view for profile page with it's forms '''
    try:
        extended_user = request.user.extendeduser  # get or create ExtendedUser
    except ExtendedUser.DoesNotExist:
        extended_user = ExtendedUser(user=request.user)
        extended_user.save()
    #profile image form
    if request.method == 'POST':
        profile_picture_form = ProfilePictureForm(request.POST, request.FILES)

        if profile_picture_form.is_valid():
            extended_user.profileImage = profile_picture_form.cleaned_data['profileImage']
            extended_user.save()
            return redirect('profile')

    else:
        profile_picture_form = ProfilePictureForm()

    # user change form
    password_change_form = PasswordChangeForm(request.user)

    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)  # Update session to prevent logout
            messages.success(request, 'Your password was successfully updated!')
            return redirect('account:profile')

    return render(request, 'account/profile.html', {'password_change_form': password_change_form,
                                                     'profile_picture_form': profile_picture_form,})