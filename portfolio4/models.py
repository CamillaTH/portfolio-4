from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.utils.text import slugify
import datetime
from datetime import date

# Create your models here.
class Category(models.Model):
    '''Model that stores categories'''
    name = models.CharField(max_length=40)
    slug = models.SlugField()
    image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering =['name']

    def __str___(self):
        return self.name

class Post(models.Model):
    '''Model that stores the post'''
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='author_posts')
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

    def like_post(self, user):
        self.likes.add(user)

    def unlike_post(self, user):
        self.likes.remove(user)
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])


class Comment(models.Model):
    '''Model that stores the comments on a post'''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='author_comment', default=None)
    content = models.TextField(blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=200, unique=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['creation_time']
    
    #override slug to make the slug unuiqe to be able to like mulitple comments
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.post}-{datetime.datetime.now()}')

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Comment {self.content} by {self.author.first_name} {self.author.last_name}"

    def amount_of_likes(self):
        return self.likes.count()

    def like_comment(self, user):
        self.likes.add(user)

    def unlike_comment(self, user):
        self.likes.remove(user)
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])


class ExtendedUser(models.Model):
    '''Model that have one2one rel with user with custom fields'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileImage = CloudinaryField('image', default='placeholder')

    def __str___(self):
        return self.user.username

    def get_profile_image(self):
        return self.profileImage.url