from rest_framework import serializers

from .models import Task, Task_Status, Categorie

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task_id', 'task_title', 'task_description', 'task_categorie', 'task_status', 'created_at', 'updated_at']


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_Status
        fields = ['task_status_id', 'task_status_description', 'created_at', 'updated_at']


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['categorie_id', 'categorie_description', 'created_at', 'updated_at']