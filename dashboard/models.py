from django.db import models

# Create your models here.

# Basic function that returns a username

# Test:


# class Username(models.Model):
#     username = models.CharField(max_length=30)
#     complete = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.username

# Actual Code:


class User(models.Model):
    # Attributes of User:
    username = models.CharField(max_length=30)
    grade = models.IntegerField(default=0)
    # subject (ignore for now)

    def __str__(self):
        return self.username+" "+str(self.grade)
