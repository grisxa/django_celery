# Generated by Django 4.1.7 on 2023-03-30 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_task_created_alter_task_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]