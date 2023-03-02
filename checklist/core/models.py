from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField()

    def __str__(self) -> str:
        return self.title

# Create your models here.
