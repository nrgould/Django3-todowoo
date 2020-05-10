from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    dateCompleted = models.DateTimeField(null=True, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    importantTask = models.BooleanField(default=False)
    taskCreator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
