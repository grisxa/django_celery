from datetime import datetime

from django.db import models


class State(models.TextChoices):
    NEW = "New"
    PENDING = "Pending"
    READY = "Ready"


class Task(models.Model):
    title = models.CharField(max_length=64)
    status = models.CharField(max_length=8, choices=State.choices, default=State.NEW)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        super().save(*args, **kwargs)

    @property
    def is_new(self):
        return self.status == State.NEW

    def __str__(self):
        return self.title
