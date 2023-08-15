from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import Group
from django.forms import inlineformset_factory
from django import forms
from .models import *
# from .forms import *
# from .decorators import unauthenticated_user, allowed_users

# @login_required(login_url='login')
# @allowed_users (allowed_roles=['students'])
def teacherui(request): 
    return render (request, 'teacherui.html')

