from django.db import models


class Todos(models.Model):
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title