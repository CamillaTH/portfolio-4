from django.contrib import admin
from .models import Comment, Post, Category
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_field = ('content')

# Register your models here.
admin.site.register(Comment)
admin.site.register(Category)
