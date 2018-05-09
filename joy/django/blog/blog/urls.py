from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
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

urlpatterns.extend(
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
