from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.

class Sector(models.Model):
    sector_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    sector_description = models.CharField(max_length=100)
    sector_active = models.BooleanField(default=True)
    sector_author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sector_Employee(models.Model):
    sector_employee_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    employee_is_manager = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
