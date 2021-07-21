from django.db import models
from django.contrib.auth.models import User


class Todos(models.Model):
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=150)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title