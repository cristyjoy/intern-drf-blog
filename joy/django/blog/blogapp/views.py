
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from blogapp.serializers import PostSerializer, TagSerializer, CategorySerializer, CommentSerializer
from .models import Post, Tag, Category, Comment

# Create your views here.



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-title')
    serializer_class = PostSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('-date_created')
    serializer_class = TagSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-date_modified')
    serializer_class = CategorySerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-post')
    serializer_class = CommentSerializer
