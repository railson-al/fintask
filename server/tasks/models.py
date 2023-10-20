from django.db import models
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField
from uuid import uuid4

from app_users.models import Sector, User
# Create your models here.

class Task_Status(models.Model):
    task_status_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    task_status_description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Task_Status_Sector(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    status = models.ForeignKey(Task_Status, on_delete=models.CASCADE) 
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Task_Priority(models.Model):
    task_priority_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    task_priority_description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Task_Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    category_description = models.CharField(max_length=100)
    category_is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Task_Category_Sector(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    category = models.ForeignKey(Task_Category, on_delete=models.CASCADE) 
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Task(models.Model):
    task_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    task_ticket = models.CharField(max_length=100, unique=True, editable=False)
    task_title = models.CharField(max_length=200)
    task_description = models.TextField()
    task_customer = models.CharField(max_length=200)
    task_is_external = models.BooleanField()
    task_status = models.ForeignKey(Task_Status, on_delete=models.CASCADE)
    task_denied_motive = models.TextField()
    task_category = models.ForeignKey(Task_Category, on_delete=models.CASCADE)
    task_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks_author", default=1)
    task_responsible = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks_responsible", default=1)
    task_has_validated = models.BooleanField(default=False)
    task_priority = models.ForeignKey(Task_Priority, on_delete=models.CASCADE)
    task_is_accepted = models.BooleanField(default=False)
    task_sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    task_deadline = models.DateTimeField()
    task_has_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = AuditlogHistoryField()

auditlog.register(Task, serialize_data=True)


class Task_Comment(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    task_comment_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    task_comment_author = models.ForeignKey(User, verbose_name=("comment_author"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)