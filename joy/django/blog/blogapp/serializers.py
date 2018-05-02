from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post, Tag, Category, Comment

# Register your models here.

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'sub_title', 'banner_photo', 'date_created', 'date_modified', 'category', 'status')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title', 'date_created', 'date_modified')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'date_created', 'date_modified')

class CommentSerializer(serializers.ModelSerializer):
    model = Comment
    fields = ('post', 'content', 'author', 'date_created')
