from .models import Tasks, Users
from .serializer import TaskSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class Task(ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer


class TaskUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
