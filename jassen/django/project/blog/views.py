from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Blog,Post,Comment,Category,Tag
from .serializers import BlogSerializer, PostSerializer,CommentSerializer,CategorySerializer,TagSerializer

class BlogViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Blog.objects.all()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)


class PostViewSet(viewsets.ViewSet):
    def list(self ,request):
        queryset = Post.objects.all()
        serializer_context = {'request': request,}
        serializer = PostSerializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    def create(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
 

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
class CommentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)
        


class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class TagViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Tag.objects.all()
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data)
        