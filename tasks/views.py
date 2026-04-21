from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()   
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'admin':
            return Task.objects.all()
        return Task.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=self.request.user)
    