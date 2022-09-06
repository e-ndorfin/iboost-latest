from django.db import models

# Create your models here.

# Basic function that returns a username


class Username(models.Model):
    username = models.CharField(max_length=30)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
