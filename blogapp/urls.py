from django.urls import path
from .views import register_user, create_blog

urlpatterns = [
    path('register_user/', register_user, name='register_user'),
    path('create_blog/', create_blog, name='create_blog'),
]
