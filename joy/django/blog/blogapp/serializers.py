from rest_framework import serializers
from .models import Post, Tag, Category, Comment

class PostSerializer(serializers.ModelSerializer):
    # tag_name = serializers.SerializerMethodField()
    # category_name = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            'title',
            'sub_title',
            'banner_photo',
            'body',
            'date_created',
            'date_modified',
            'category',
            'tags',
            'status'
        )
    # def get_category_name(self, instance):
    #     return instance.category.title

    # def get_tag_name(self, instance):
    #     return instance.tags.title

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
