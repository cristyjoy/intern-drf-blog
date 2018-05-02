from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post, Tag, Category, Comment

class PostSerializer(serializers.ModelSerializer):
   class Meta:
       model = Post
       fields = ('title', 'sub_Title', 'banner_Photo', 'date_created', 'category', 'status')

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

