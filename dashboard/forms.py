from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class GradesForm(ModelForm):
    class Meta:
        model = Grade
        fields = ['subject', 'criterionA',
                  'criterionB', 'criterionC', 'criterionD', 'srr']


# class SRRForm(ModelForm):
#     class Meta:
#         model = Grade
#         fields = ['srr']
