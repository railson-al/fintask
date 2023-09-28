# Generated by Django 4.2.5 on 2023-09-28 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0003_rename_categories_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tasks_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='task_responsible',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tasks_responsible', to=settings.AUTH_USER_MODEL),
        ),
    ]