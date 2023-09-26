from django.db import models
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)