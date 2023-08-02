from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms.widgets import *
from django.contrib.auth.models import User
from teacherui.models import *

from .models import *


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class GradesForm(ModelForm):
    class Meta:
        model = Grade
        fields = ['subject', 'criterionA',
                  'criterionB', 'criterionC', 'criterionD']


class SRRForm(ModelForm):
    ATL_CHOICES = (
        ('Interaction', 'Interaction'),
        ('Language', 'Language'),
        ('Collaboration', 'Collaboration'),
        ('Information Literacy', 'Information Literacy'),
        ('Media Literacy', 'Media Literacy'),
        ('Affective Skills', 'Affective Skills'),
        ('Organizational Skills', 'Organizational Skills'),
        ('Reflection', 'Reflection'),
        ('Critical Thinking', 'Critical Thinking'),
        ('Creative Thinking', 'Creative Thinking'),
        ('Transfer', 'Transfer'),
    )
    bestatl = forms.ChoiceField(choices=ATL_CHOICES)
    worstatl = forms.ChoiceField(choices=ATL_CHOICES)
    class Meta:
        model = SRR
        fields = ['srr', 'title', 'bestatl', 'worstatl','profile']
        widgets = {
          'title': forms.Textarea(attrs={'rows':1, 'cols':40}),
        }

class JoinClassForm(ModelForm):
    class Meta:
        model = Student
        fields = ['klass']

class EditProfileForm(forms.Form):
    class Meta:
        cpassword=forms.CharField(label='cPassword', max_length=200)
        npassword=forms.CharField(label='nPassword', max_length=200)
        npassword2=forms.CharField(label='nPassword2', max_length=200)
        fields = ['cpassword','npassword','npassword2']