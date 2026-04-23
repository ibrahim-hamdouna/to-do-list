from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tasks(models.Model):
    """
    Represents a task in the to-do list to specific user.
    Tracks tasks that the user needs to complete, and keeps track of when the task was created and last updated.
    """
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.description