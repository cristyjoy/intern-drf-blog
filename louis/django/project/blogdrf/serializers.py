from rest_framework import serializers

from .models import Category, Tag, Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'title',
            'date_created',
            'date_modified'
        )

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'title',
            'date_created',
            'date_modified'
        )

class PostSerializer(serializers.ModelSerializer):
    tag_name = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            'title',
            'subtitle',
            'banner_photo',
            'tags',
            'tag_name',
            'category',
            'category_name',
            'body',
            'status',
            'date_created',
            'date_modified'
        )

    def get_category_name(self, instance):
        return instance.category.title

    def get_tag_name(self, instance):
        return instance.tags.title

    # def create(self, validated_data):
    #     category_data = validated_data.pop('category')
    #     category = Album.objects.create(**validated_data)
    #     for category_data in category_data:
    #         Track.objects.create(category=category, **category_data)
    #     return category
