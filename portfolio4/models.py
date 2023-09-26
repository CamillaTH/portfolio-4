from django.db import models
from django.conf import settings

# Create your models here.

#Model that stores the comments on a post
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    comment = models.CharField(max_length=350, null=False, blank=False)

    def __str__(self):
        return str(self.author)

#Model that stores the likes om a comment
class CommentLike(models.Model):
     author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
     comment = models.ForeignKey(Comment,on_delete=models.CASCADE,)
     likes = models.IntegerField()
     
     def __str__(self):
        return str(self.author)

#Model that stores the post
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE,null=True, blank=True)
    post = models.CharField(max_length=900, null=False, blank=False)

    def __str__(self):
        return str(self.author)

