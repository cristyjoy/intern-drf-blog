from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Blog,Post,Comment,Category,Tag


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ('heading', 
                  'sub_heading')

class PostSerializer(serializers.ModelSerializer):
    blog = serializers.SlugRelatedField(read_only=True, slug_field='heading')
    category = serializers.SlugRelatedField(read_only=True, slug_field='title')
 
    class Meta:
        model = Post
        fields = ('title',
                  'sub_title', 
                  'banner_photo', 
                  'body', 
                  'date_modified', 
                  'blog',
                  'category',
                  'tags', 
                  'status')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 
                  'text')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title',)

 