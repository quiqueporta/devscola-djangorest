from django.conf import settings
from django.db import models


class Task(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="tasks", on_delete=models.CASCADE)
    notes = models.CharField(max_length=500, blank=False, null=False)
    due_date = models.DateField(blank=True, null=True)
    done = models.BooleanField(blank=True, null=False, default=False)

    def __str__(self):
        return self.notes

    def mark_as_done(self):
        self.done = True
