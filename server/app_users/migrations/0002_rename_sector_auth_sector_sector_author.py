# Generated by Django 4.2.5 on 2023-09-29 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sector',
            old_name='sector_auth',
            new_name='sector_author',
        ),
    ]
