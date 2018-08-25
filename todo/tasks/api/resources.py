from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Task
from .serializers import TaskSerializer
from .permissions import IsOwnerOrDeny


class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrDeny)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
