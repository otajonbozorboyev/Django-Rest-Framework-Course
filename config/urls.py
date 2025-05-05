from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings


urlpatterns = (
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
)