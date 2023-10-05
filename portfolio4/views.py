from django.shortcuts import render,  HttpResponse, redirect
from .models import  Post, Comment, Category
from .forms import PostForm
from django.views import generic, View
# Create your views here.

'''
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
'''
class CategoryList(generic.ListView):
    ''' '''
    model = Category
    queryset = Category.objects.order_by('name')
    template_name = 'index.html'
    paginate_by = 10

class PostList(generic.ListView):
    ''' '''
    model = Post
    queryset = Post.objects.order_by('creation_time')
    template_name = 'index.html'
    paginate_by = 5

class CategoryDetail(View):
    ''' '''
    def get(self, request, slug, *args, **kwargs):
        queryset = Category.objects
        categories = get_object_or_404(queryset, slug=slug)

    pass