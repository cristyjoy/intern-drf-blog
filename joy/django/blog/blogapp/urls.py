from django.contrib import admin
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from blogapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^post/$', views.PostViewSet.as_view()),
    url(r'^post/(?P<pk>[0-9+])/$', views.PostViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
