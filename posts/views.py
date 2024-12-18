from .serializers import PostSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .permissions import IsAuthorOrReadOnly


class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
