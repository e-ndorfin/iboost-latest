from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=200, null=True)
    school = models.CharField(max_length=200, null=True)
    num_classes = models.IntegerField(default=0, null=True)
    def __str__(self):
        return self.username

class Klass(models.Model):
    classname = models.CharField(max_length=100, null=True)
    teachers = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.classname

class Student(models.Model):
    # Database Fields
    profile = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    klass = models.ForeignKey(Klass, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name