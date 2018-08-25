from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from ..models import Task
from .serializers import TaskSerializer
from .permissions import IsOwnerOrDeny


class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrDeny)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TasksDoneViewSet(viewsets.ViewSet):

    def done(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)

        task.mark_as_done()
        task.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


done = TasksDoneViewSet.as_view({'patch': 'done'})
