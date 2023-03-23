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

# Create your views here.
from .models import *
from .forms import *
from .decorators import unauthenticated_user, allowed_users


@login_required(login_url='login')
@allowed_users(allowed_roles=['students'])
def index(request):
    subjects = request.user.profile.subject_set.all()
    grades = request.user.profile.subject_set.all()[1].grade_set.all()
    # Grade form
    gradeform = GradesForm()
    if request.method == 'POST':
        # Add grades
        gradeform = GradesForm(request.POST)
        if gradeform.is_valid():
            gradeform.save()
    
    #Graph stuff
    labels = ["January", "Febuary", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    data = [0,0,0,0,0,0,0,0,0,0,0,0]
    avggrade = [0,0,0,0,0,0,0,0,0,0,0,0]
    monthgradecount = [0,0,0,0,0,0,0,0,0,0,0,0]
    average = 0
    month = 0
    for i in range(len(request.user.profile.subject_set.all())):
        for grade in request.user.profile.subject_set.all()[i].grade_set.all():
            avg = (grade.criterionA+grade.criterionB +
                grade.criterionC+grade.criterionD)/4
            month = grade.created.month
            monthgradecount[month-1] += 1
            avggrade[month-1] += avg
            data[month-1] = avggrade[month-1]/monthgradecount[month-1]

    return render(request, 'dashboard/index.html', {
        "subjects": subjects,
        "gradeform": gradeform,
        'labels': labels, 
        'data': data
    })


# Login and Register Function
SUBJECT_CHOICES = [
    ('', 'Subject '), ('Chinese', "Chinese"), ('English', "English"), ('Math', "Math"), ('Science', "Science"), ('Individuals and Societies', "Individuals and Societies"), ('Music',
                                                                                                                                                                             "Music"), ('Drama', "Drama"), ('Art', "Art"), ('MYP Physical Education', "MYP Physical Education"), ('Design', "Design"), ('Computer Science', "Computer Science")
]


# def main_chart(request):
#     labels = ["January", "Febuary", "March", "April", "May", "June",
#               "July", "August", "September", "October", "November", "December"]
#     data = [0,0,0,0,0,0,0,0,0,0,0,0]
#     print(len(request.user.profile.subject_set.all()))
#     for i in range(len(request.user.profile.subject_set.all())):
#         for grade in request.user.profile.subject_set.all()[i].grade_set.all():
#             avg = (grade.criterionA+grade.criterionB +
#                 grade.criterionC+grade.criterionD)/4
#             month = grade.created.month
#             data[month-1] = avg

#     return render(request, 'dashboard/mainchart.html', {
#         'labels': labels, 
#         'data': data
#     })


@unauthenticated_user
def registerPage(request):
    form = RegisterUserForm()
    SubjectFormSet = inlineformset_factory(
        Profile, Subject, fields=('subjectname',), extra=6, widgets={'subjectname': forms.Select(choices=SUBJECT_CHOICES)},)
    formset = SubjectFormSet()
    # If the user is registering an account
    if request.method == "POST":
        # For registering the account
        if request.POST.get('submit') == 'Register Account':
            form = RegisterUserForm(request.POST)
            if form.is_valid():  # If the password is valid, save
                user = form.save()
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                group = Group.objects.get(name="students")
                user.groups.add(group)
                Profile.objects.create(
                    user=user, username=username, email=email)
                profile = Profile.objects.get(username=username)

                # Add subjects
                formset = SubjectFormSet(
                    request.POST, instance=profile)
                if formset.is_valid():
                    formset.save()
                messages.success(
                    request, 'Account was created for ' + username)
                return redirect('login')
    context = {'form': form, 'formset': formset}
    return render(request, 'dashboard/accountcreation.html', context)


@ unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        usernamereq = request.POST.get('username')
        passwordreq = request.POST.get('password')
        user = authenticate(
            request, username=usernamereq, password=passwordreq)
        print(user)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:  # If username/password is incorrect
            messages.info(
                request, 'Sorry, your username or password was incorrect. Please try again.')
            return render(request, 'dashboard/accountcreation.html', {})
    context = {}
    return render(request, 'dashboard/login.html', context)


@ login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect(reverse('login'))


@ login_required(login_url='login')
@ allowed_users(allowed_roles=['students'])
def improvements(request):
    return render(request,  'dashboard/improvements1.html', {})


@ login_required(login_url='login')
def base(request):
    return render(request, 'dashboard/base.html', )


@ login_required(login_url='login')
@ allowed_users(allowed_roles=['students'])
def grades(request):
    return render(request, 'dashboard/grades.html')


@ login_required(login_url='login')
@ allowed_users(allowed_roles=['students'])
def improvements2(request):
    return render(request, 'dashboard/improvements2.html')


@ login_required(login_url='login')
@ allowed_users(allowed_roles=['students'])
def improvements3(request):
    return render(request, 'dashboard/improvements3.html')


@ login_required(login_url='login')
@ allowed_users(allowed_roles=['students'])
def profile(request):
    return render(request, 'dashboard/profile.html',)


@ login_required(login_url='login')
@ allowed_users(allowed_roles=['students'])
def login(request):
    return render(request, 'dashboard/login.html')


@ login_required(login_url='login')
@ allowed_users(allowed_roles=['students'])
def testing(request):
    grades = Grade.objects.all()
    subjectname = Subject.objects.all()
    return render(request, 'dashboard/testing.html', {'grades': grades, 'subjectname': subjectname},)


@ login_required(login_url='login')
def chineseg(request):
    return render(request, 'dashboard/chinese.html')


def modaltest(request):
    return render(request, 'dashboard/modaltest.html',)


def accountcreation(request):
    return render(request, 'dashboard/accountcreation.html',)


def radialtest(request):
    return render(request, 'dashboard/gradestest.html',)


def accountcreation(request):
    return render(request, 'dashboard/accountcreation.html',)

def interviewarchive(request):
    return render(request, 'dashboard/interviewarchive.html')