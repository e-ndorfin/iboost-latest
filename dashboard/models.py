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
    # Database Fields
    username = models.CharField(max_length=30, null=True)
    # subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.username


class Subject(models.Model):
    # Database fields
    # User has a "One to Many" relationship with Subject, as one User can have multiple subjects,while the opposite is not the case
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    subjectname = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.subjectname


class Grade(models.Model):  # Subject has a "One to Many" relationship with Grade, as one User can have multiple subjects,while the opposite is not the case
    # Database fields
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    criterionA = models.IntegerField(default=0, null=True)
    criterionB = models.IntegerField(default=0, null=True)
    criterionC = models.IntegerField(default=0, null=True)
    criterionD = models.IntegerField(default=0, null=True)

    def __str__(self):
        return "A:%i B:%i C:%i D:%i" % (self.criterionA, self.criterionB, self.criterionC, self.criterionD)
