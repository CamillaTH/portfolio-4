from django.contrib import admin
from .models import Comment, Post, Category
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('heading',)}
    summernote_field = ('content')
    list_filter = ('approved', 'creation_time')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name',)


# Register your models here.
admin.site.register(Comment)