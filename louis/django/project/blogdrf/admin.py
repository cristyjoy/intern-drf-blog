from django.contrib import admin

from .models import Category, Tag, Post

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'date_modified')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'date_modified')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date_created', 'date_modified')
