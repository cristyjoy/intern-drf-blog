from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from blogapp import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet, base_name='post')
router.register(r'tags', views.TagViewSet, base_name='tag')
router.register(r'categorys', views.CategoryViewSet, base_name='category')
router.register(r'comments', views.CommentViewSet, base_name='comment')



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
