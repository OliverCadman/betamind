from django.contrib import admin
from django.conf import settings

from .models import Mood, Post, Comment


@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    list_display = ['mood', 'slug']
    prepopulated_fields = {'slug': ('mood',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'post_sender', 'created_at']
    list_filter = ['post_sender', 'title', 'created_at']
    search_fields = ['title', 'content', 'post_sender']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_sender', 'post', 'create_post', 'comment']
    list_filter = ['comment', 'comment_sender', 'post']
    search_fields = ['comment_sender', 'comment', 'create_post']
