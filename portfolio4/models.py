from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone
import datetime

# Create your models here.

#Model that stores the post
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='author_posts')
    #comment = models.ForeignKey(Comment,on_delete=models.CASCADE,null=True, blank=True)
    heading = models.CharField(max_length=150, unique=True)
    content = models.TextField(blank=True)
    creationTime = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    class Meta:
        ordering =['-creationTime']

    def __str__(self):
        return str(self.title)

    def amount_of_likes(self):
        return self.likes.count()

#Model that stores the comments on a post
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    #author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='author_comment')
    content = models.TextField(blank=True)
    creationTime = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['creationTime']

    def __str__(self):
        return f"Comment {self.content} by "#{self.author.first_name} {self.author.last_name}"

#Model that stores the likes on a comment
#class CommentLike(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
#     comment = models.ForeignKey(Comment,on_delete=models.CASCADE,)
#     likes = models.IntegerField()
#     
#     def __str__(self):
#        return str(self.author)