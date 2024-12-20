from django.urls import path
from .views import register_user, create_blog, blog_list, update_blog, delete_blog, update_user_profile

urlpatterns = [
    path('register_user/', register_user, name='register_user'),
    path('create_blog/', create_blog, name='create_blog'),
    path('blog_list/', blog_list, name='blog_list'),
    path('update_blog/<int:pk>/', update_blog, name='update_blog'),
    path('delete_blog/<int:pk>/', delete_blog, name='delete_blog'),
    path('update_user/', update_user_profile, name='update_user'),
]
