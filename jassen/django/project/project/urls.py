"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.conf.urls import url, include
from rest_framework import routers
from blog import views 
from blog.views import BlogViewSet,PostViewSet,CommentViewSet,CategoryViewSet,TagViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register(r'blogs', BlogViewSet, base_name='blog')
router.register(r'posts', PostViewSet, base_name='post')
router.register(r'comments', CommentViewSet, base_name='comment')
router.register(r'category', CategoryViewSet, base_name='category')
router.register(r'tags', TagViewSet, base_name='tag')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)