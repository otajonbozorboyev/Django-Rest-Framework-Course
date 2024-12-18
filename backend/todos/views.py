from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Todo
from .serializers import TodoSerializer


class ListTodo(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer