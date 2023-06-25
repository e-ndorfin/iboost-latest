from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms.widgets import *
from django.contrib.auth.models import User

from .models import *

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RegisterTeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['school', 'num_classes']

class AddClassForm(ModelForm):
    class Meta:
        model = Klass
        fields = ['classname', 'teachers']