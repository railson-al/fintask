from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from uuid import uuid4

# Create your models here.
class User(AbstractBaseUser):
    
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'


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
