from rest_framework import serializers

from ..models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'notes', 'due_date', 'done', 'url')
        read_only_fields = ('done',)
