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
from .forms import *
from .decorators import unauthenticated_user, allowed_users

# @login_required(login_url='login')
# @allowed_users (allowed_roles=['students'])

@allowed_users (allowed_roles=['teachers'])
def base(request): 
    return render (request, 'base.html')


@allowed_users(allowed_roles=['teachers'])
def teacherui(request): 
    classes = request.user.teacher.klass_set.all():

    
    #Add Classes
    classform = AddClassForm()
    if request.method == 'POST':
        classform = AddClassForm(request.POST)
        if classform.is_valid():
            classform.save()
    return render (request, 'teacherui.html', {'classes':classes, 'classform':classform})


@allowed_users(allowed_roles=['teachers'])
def teacherclass(request):
    return render (request, 'teacherclass.html')

def teacheraccountcreation(request):
    form = RegisterUserForm()
    teacherform = RegisterTeacherForm()
    # If the user is registering an account
    if request.method == "POST":
        # For registering the account
        if request.POST.get('submit') == 'Register Account':
            teacherform = RegisterTeacherForm(request.POST)
            form = RegisterUserForm(request.POST)
            print("test1")
            print(form.errors)
            if form.is_valid():  # If the password is valid, save
                print("test")
                user = form.save()
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                group = Group.objects.get(name="teachers")
                user.groups.add(group)
                school = teacherform.data.get('school')
                num_classes = teacherform.data.get('num_classes')
                Teacher.objects.create(
                    user=user, username=username, email=email, school=school, num_classes=num_classes)
                messages.success(
                    request, 'Account was created for ' + username)
                return redirect('login')
    context = {'form': form, 'teacherform':teacherform}
    return render(request, 'teacheraccountcreation.html', context)
