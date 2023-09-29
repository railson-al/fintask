from rest_framework import serializers
from auditlog.models import LogEntry

from tasks.models import Task, Task_Status, Categorie

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task_id', 'task_title', 'task_description', 'task_categorie', 
                  'task_status', 'task_author', 'task_responsible', 'task_is_accepted', 'created_at', 'updated_at']


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_Status
        fields = ['task_status_id', 'task_status_description', 'created_at', 'updated_at']


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['categorie_id', 'categorie_description', 'created_at', 'updated_at']


class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        # fields = '__all__'
        fields = ['id', 'object_pk', 'changes', 'timestamp', 'content_type']