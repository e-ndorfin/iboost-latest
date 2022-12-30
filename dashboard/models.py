from django.db import models
from django.contrib.auth.models import User


class Grade(models.Model):
    # Database fields
    # Subject has a "One to Many" relationship with Grade, as one User can have multiple subjects,while the opposite is not the case
    criterionA = models.IntegerField(default=0, null=True)
    criterionB = models.IntegerField(default=0, null=True)
    criterionC = models.IntegerField(default=0, null=True)
    criterionD = models.IntegerField(default=0, null=True)

    def __str__(self):
        return "A:%i B:%i C:%i D:%i" % (self.criterionA, self.criterionB, self.criterionC, self.criterionD)


class Subject(models.Model):
    # Database fields
    # User has a "One to Many" relationship with Subject, as one User can have multiple subjects,while the opposite is not the case
    subjectname = models.CharField(max_length=30, null=True)
    grades = models.ForeignKey(Grade, null=True, on_delete=models.CASCADE)
    srr = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.subjectname


class Profile(models.Model):
    # Database Fields
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=200, null=True)
    subjects = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    # subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.username
