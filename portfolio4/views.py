from django.shortcuts import render,  HttpResponse

# Create your views here.
def get_home_page(request):
    return render(request, 'portfolio4/home_page.html')