# Generated by Django 4.1.7 on 2023-03-30 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_created_alter_task_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 30, 12, 51, 13, 805058)),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
