from django.db import models
from django.conf import settings


class Priority(models.Model):
    priority = models.CharField(max_length=20)

    def __str__(self):
        return self.priority


class Task(models.Model):
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    date_task = models.DateField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    changed = models.DateField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    priority = models.ForeignKey(
        Priority,
        on_delete=models.CASCADE
    )
    event = models.CharField(max_length=50, default=None)

    def __str__(self):
        return 'Name: {}, Done: {}, User: {}, Priority: {}'.format(
            self.name,
            self.done,
            self.user,
            self.priority
        )
