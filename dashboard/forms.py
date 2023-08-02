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
    subject = forms.ModelChoiceField(queryset=Subject.objects.none())
    class Meta:
        model = Grade
        fields = ['subject', 'criterionA',
                  'criterionB', 'criterionC', 'criterionD']

    def __init__(self, *args, **kwargs):
        curr_user = kwargs.pop('curr_user', None)
        print(curr_user)
        super().__init__(*args, **kwargs)
        self.fields['subject'].queryset = Subject.objects.filter(
            profile__user=curr_user)


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

