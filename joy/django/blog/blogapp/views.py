from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from blogapp.serializers import PostSerializer, TagSerializer, CategorySerializer, CommentSerializer
from .models import Post, Tag, Category, Comment
from rest_framework import permissions

class PostViewSet(viewsets.ViewSet):
      def list(self, request):
          queryset = Post.objects.all()
          serializer = PostSerializer(queryset, many=True)
          return Response(serializer.data)

      def retrieve(self, request, pk=None):
          queryset = Post.objects.all()
          post = get_object_or_404(queryset, pk=pk)
          serializer = PostSerializer(post)
          return Response(serializer.data)

class TagViewSet(viewsets.ViewSet):
      def list(self, request):
          queryset = Tag.objects.all()
          serializer = TagSerializer(queryset, many=True)
          return Response(serializer.data)

class CategoryViewSet(viewsets.ViewSet):
      def list(self, request):
          queryset = Category.objects.all()
          serializer = CategorySerializer(queryset, many=True)
          return Response(serializer.data)

class CommentViewSet(viewsets.ViewSet):
      def list(self, request):
          queryset = Comment.objects.all()
          serializer = CommentSerializer(queryset, many=True)
          return Response(serializer.data)
# class ExpiringTokenAuthentication(permissions.BasePermission):

#       def has_permission(self, request, view):
#           if request.method == 'PUT':
#             class Signup(APIView):
#               permission_classes = (IsAuthenticatedOrReadOnly,)

  # from rest_framework import status
  # from rest_framework.decorators import api_view
  # from rest_framework.response import Response
  # from blogapp.models import Post
  # from blogapp.serializers import PostSerializer

  # @api_view(['GET', 'POST'])
  # def post_list(request, format=None):

  #     if request.method == 'GET':
  #         post = Post.objects.all()
  #         post = PostSerializer(post, many=True)
  #         return Response(serializer.data)

  #     elif request.method == 'POST':
  #         serializer = PostSerializer(data=request.data)
  #         if serializer.is_valid():
  #             serializer.save()
  #             return Response(serializer.data, status=status.HTTP_201_CREATED)
  #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  # @api_view(['GET', 'PUT', 'DELETE'])
  # def post_detail(request, title, format=None):
  #     try:
  #         post = Post.objects.get(title=title)
  #     except Post.DoesNotExist:
  #         return Response(status=status.HTTP_400_NOT_FOUND)

  #     if request.method == 'GET':
  #         serializer = PostSerializer(post, data=request.data)
  #         if serializer.is_valid():
  #             serializer.save()
  #             return Response(serializer.data)
  #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  #     elif request.method == 'DELETE':
  #         post.delete()
  #         return Response(status=status.HTTP_204_NO_CONTENT)
