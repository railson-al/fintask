# Generated by Django 4.2.5 on 2023-09-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_task_author_task_task_responsible'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_is_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
