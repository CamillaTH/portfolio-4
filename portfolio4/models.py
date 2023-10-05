from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone
import datetime

# Create your models here.
class Category(models.Model):
    '''Model that stores categories'''
    name = models.CharField(max_length=40)
    slug = models.SlugField()
    image = CloudinaryField('image', default='placeholder')
    #creation_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['name']

    def __str___(self):
        return self.name

class Post(models.Model):
    '''Model that stores the post'''
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='author_posts')
    #comment = models.ForeignKey(Comment,on_delete=models.CASCADE,null=True, blank=True)
    heading = models.CharField(max_length=150, unique=True)
    content = models.TextField(blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering =['-creation_time']

    def __str__(self):
        return str(self.heading)

    def amount_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    '''Model that stores the comments on a post'''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    #author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='author_comment')
    content = models.TextField(blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField()

    class Meta:
        ordering = ['creation_time']

    def __str__(self):
        return f"Comment {self.content} by "#{self.author.first_name} {self.author.last_name}"