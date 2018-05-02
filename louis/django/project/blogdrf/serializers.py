from rest_framework import serializers

from .models import Category, Tag, Post

class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="category-detail")
    class Meta:
        model = Category
        fields = (
            'url',
            'title',
            'date_created',
            'date_modified'
        )

class TagSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="tag-detail")
    class Meta:
        model = Tag
        fields = (
            'title',
            'date_created',
            'date_modified'
        )

class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="post-detail")
    class Meta:
        model = Post
        fields = (
            'url',
            'title',
            'subtitle',
            'banner_photo',
            'tags',
            'category',
            'body',
            'status',
            'date_created',
            'date_modified'
        )
