from django.db import models
from django.contrib.auth.models import User
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField
from uuid import uuid4

# Create your models here.

class Task_Status(models.Model):
    task_status_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    task_status_description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Categorie(models.Model):
    categorie_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    categorie_description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Task(models.Model):
    task_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    task_title = models.CharField(max_length=200)
    task_description = models.TextField()
    task_categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    task_status = models.ForeignKey(Task_Status, on_delete=models.CASCADE)
    task_auth = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks_author")
    task_resposible = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks_responsible")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = AuditlogHistoryField()

auditlog.register(Task, serialize_data=True)