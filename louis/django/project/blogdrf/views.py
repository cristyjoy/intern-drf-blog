from django.shortcuts import get_object_or_404

from django.shortcuts import render

from django.http import Http404

from rest_framework import viewsets, status

from rest_framework.response import Response

from .models import Category, Tag, Post

from .serializers import CategorySerializer, TagSerializer, PostSerializer

# Create your views here.

class CategoryViewSet(viewsets.ViewSet):
    def list(self ,request):
        queryset = Category.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = CategorySerializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer_context = {
            'request': request,
        }
        serializer = CategorySerializer(category, context=serializer_context)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagViewSet(viewsets.ViewSet):
    def list(self ,request):
        queryset = Tag.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = TagSerializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Tag.objects.all()
        tag = get_object_or_404(queryset, pk=pk)
        serializer_context = {
            'request': request,
        }
        serializer = TagSerializer(tag, context=serializer_context)
        return Response(serializer.data)

class PostViewSet(viewsets.ViewSet):
    def list(self ,request):
        queryset = Post.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = PostSerializer(queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer_context = {
            'request': request,
        }
        serializer = PostSerializer(post, context=serializer_context)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
