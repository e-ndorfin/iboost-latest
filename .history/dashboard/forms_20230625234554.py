from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms.widgets import *
from django.contrib.auth.models import User

from .models import *
from teacherui.models import * 


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class GradesForm(ModelForm):
    class Meta:
        model = Grade
        fields = ['subject', 'criterionA',
                  'criterionB', 'criterionC', 'criterionD']
        
class klassForm(ModelForm): 
    def __init__(classes): 
        classField = forms.ChoiceField(choices=classes)
    class Meta: 
        model = Klass
        fields = None 
        # fields = [(name, name) for name in MyModel.objects.values_list('name', flat=True)]
        # name = forms.ChoiceField(choices=name_choices)


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
