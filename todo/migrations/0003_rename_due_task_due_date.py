# Generated by Django 4.1.3 on 2022-12-11 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_task_due'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='due',
            new_name='due_date',
        ),
    ]
