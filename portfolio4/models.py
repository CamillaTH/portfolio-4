from django.db import models
from django.conf import settings
# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    comment = models.CharField(max_length=350, null=False, blank=False)