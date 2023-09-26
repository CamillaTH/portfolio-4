from django.contrib import admin
from .models import Comment
from .models import CommentLike
from .models import Post
# Register your models here.
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(Post)