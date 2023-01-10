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
from .forms import RegisterUserForm
from .decorators import unauthenticated_user, allowed_users


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    def get_providers(self):
        """Return names of datasets."""
        return ["English", "Chinese", "Chemistry"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[0, 0, 0, 4, 6, 5, 7, 4, 4, 4, 6, 7],
                [0, 0, 0, 4, 5, 6, 7, 4, 7, 4, 7, 8, 8],
                [0, 0, 0, 5, 7, 4, 6, 7, 8, 8, 8, 8, 8]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()


@login_required(login_url='login')
@allowed_users(allowed_roles=['students'])
def index(request):
    profile = request.user.profile.subject_set.all()
    print(profile)
    context = {"profile": profile}
    return render(request, 'dashboard/index.html', context)


# Login and Register Function
SUBJECT_CHOICES = [
    ('chinese', "Chinese"), ('english', "English"), ('math', "Math"), ('science', "Science"), ('ins', "Individuals and Societies"), ('music',
                                                                                                                                     "Music"), ('drama', "Drama"), ('art', "Art"), ('PE', "MYP Physical Education"), ('DT', "Design"), ('CS', "Computer Science")
]


@unauthenticated_user
def registerPage(request):
    form = RegisterUserForm()
    SubjectFormSet = inlineformset_factory(
        Profile, Subject, fields=('subjectname',), extra=6, widgets={'subjectname': forms.Select(choices=SUBJECT_CHOICES)})
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
