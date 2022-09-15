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
class Subject(models.Model):
    #Database fields
    subjectname = models.CharField(max_length=30)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.subjectname+" Score: "+str(self.score)

class User(models.Model):
    # Database Fields
    username = models.CharField(max_length=30)
    grade = models.IntegerField(default=0)
    subjects = models.ManyToManyField(Subject)
    # # subject (ignore for now)

    def __str__(self):
        return self.username+" "+str(self.grade)


