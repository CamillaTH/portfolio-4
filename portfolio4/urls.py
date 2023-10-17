"""protfolio4_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path("", views.CategoryList.as_view(), name="category"),
    #path("", views.PostList.as_view(), name="posts_home"),
    path("", views.Home_items, name="home"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/like/', views.like_post, name='like_post'),
    path('comment/<slug:slug>/like/', views.like_comment, name='like_comment'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
