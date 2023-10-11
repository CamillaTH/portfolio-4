from django.contrib import admin
from .models import Comment, Post, Category, ExtendedUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('heading',)}
    summernote_field = ('content')
    list_display = ('heading', 'slug', 'approved', 'creation_time')
    list_filter = ('approved', 'creation_time')
    search_fields = ('categories', 'heading')
    actions = ['approve_Posts']
    
    def approve_Posts(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name',)
    search_fields = ('name',)
    list_display = ('name', 'slug')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    summernote_field = ('content')
    prepopulated_fields = {'slug': ('post',)}
    list_display = ('content', 'post', 'creation_time', 'approved')
    list_filter = ('approved', 'creation_time')
    search_fields = ('author', 'content')

    actions = ['approve_Comments']
    
    def approve_Comments(self, request, queryset):
        queryset.update(approved=True)

class ExtendedUserInline(admin.StackedInline):
    model = ExtendedUser 
    can_delete = False
    verbose_name_plural = 'Extended users'

class customUserAdmin(UserAdmin):
    inlines = (ExtendedUserInline, )

admin.site.unregister(User)
admin.site.register(User, customUserAdmin)