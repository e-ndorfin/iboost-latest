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
import logging

# Create your views here.
from .models import *
from .forms import *
from .decorators import unauthenticated_user, allowed_users, return_user

logger = logging.getLogger(__name__)


@login_required(login_url='login')
@allowed_users(allowed_roles=['students'])
def index(request):
    subjects = request.user.profile.subject_set.all()
    grades = request.user.profile.subject_set.all()[1].grade_set.all()
    # Grade form
    gradeform = GradesForm()
    srrform = SRRForm()
    if request.method == 'POST':
        # Add grades
        srrform = SRRForm(request.POST)
        gradeform = GradesForm(request.POST)
        if gradeform.is_valid() and srrform.is_valid():
            srrform.save().grade = gradeform.save(commit=False)
            gradeform.save()
            srrform.save()
    # Graph stuff
    labels = ["January", "Febuary", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    datamain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    avggrade = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    monthgradecount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    sortavg = []
    bestworst = [0, 0]
    grades = []
    month = 0
    databest = [0, 0, 0, 0, 0, 0]
    dataworst = [0, 0, 0, 0, 0, 0]
    labelsbest = ["Criterion A", "Criterion B", "Criterion C",
                  "Criterion D", "Grade Average", "Subject Average"]
    labelsworst = ["Criterion A", "Criterion B", "Criterion C",
                   "Criterion D", "Grade Average", "Subject Average"]
    labelsradar = []
    dataradar = [0, 0, 0, 0, 0, 0]

    # Calculate average for each month
    for i in range(len(request.user.profile.subject_set.all())):
        for grade in request.user.profile.subject_set.all()[i].grade_set.all():
            avg = (grade.criterionA+grade.criterionB +
                   grade.criterionC+grade.criterionD)/4
            grade.avg = avg
            grade.save()
            month = grade.created.month
            monthgradecount[month-1] += 1
            avggrade[month-1] += avg
            datamain[month-1] = avggrade[month-1]/monthgradecount[month-1]

    # Calculate average for each subject
    subjects = request.user.profile.subject_set.all()
    subjectavg = 0
    i = 0
    for subject in subjects:
        labelsradar.append(subject.subjectname)
        for grade in subject.grade_set.all():
            subjectavg += grade.avg
        if len(subject.grade_set.all()) != 0:
            subjectavg = subjectavg/len(subject.grade_set.all())
        subject.subjectavg = subjectavg
        subject.save()
        dataradar[i] = float(subjectavg)
        i += 1
        subjectavg = 0

    # Find best and worst subjects
    for k in range(len(request.user.profile.subject_set.all())):
        for grade in request.user.profile.subject_set.all()[k].grade_set.all():
            sortavg.append(grade.avg)
        # Sort
        for i in range(1, len(sortavg)):
            key = sortavg[i]
            k = i-1
            while k >= 0 and sortavg[k] > key:
                sortavg[k+1] = sortavg[k]
                k -= 1
            sortavg[k+1] = key

    # Add best/worst:
    for r in range(len(request.user.profile.subject_set.all())):
        if (request.user.profile.subject_set.all()[r].grade_set.all().exists() == True):
            for grade in request.user.profile.subject_set.all()[r].grade_set.all():
                grades.append(grade)
    for p in range(len(grades)):
        if grades[p].avg == sortavg[0]:
            bestworst[0] = grades[p]
        elif grades[p].avg == sortavg[len(sortavg)-1]:
            bestworst[1] = grades[p]

    if bestworst[0] != 0 and bestworst[1] != 0:
        # Set best:
        databest[0] = bestworst[1].criterionA
        databest[1] = bestworst[1].criterionB
        databest[2] = bestworst[1].criterionC
        databest[3] = bestworst[1].criterionD
        databest[4] = float(bestworst[1].avg)
        databest[5] = float(bestworst[1].subject.subjectavg)

        # Set worst:
        dataworst[0] = bestworst[0].criterionA
        dataworst[1] = bestworst[0].criterionB
        dataworst[2] = bestworst[0].criterionC
        dataworst[3] = bestworst[0].criterionD
        dataworst[4] = float(bestworst[0].avg)
        dataworst[5] = float(bestworst[0].subject.subjectavg)

    #Join Classes
    user = request.user
    logger.warning(user)
    joinclassform = JoinClassForm()
    if request.method == 'POST':
        joinclassform = JoinClassForm(request.POST)
        logger.warning(joinclassform)
        logger.warning('hi')
        if joinclassform.is_valid():
            joinclassform.save()

    return render(request, 'dashboard/index.html', {
        "subjects": subjects,
        "gradeform": gradeform,
        'srrform': srrform, 
        'labels': labels,
        'data': datamain,
        'bestworst': bestworst,
        'labelsbest': labelsbest,
        'databest': databest,
        'labelsworst': labelsworst,
        'dataworst': dataworst,
        'dataradar': dataradar,
        'labelsradar': labelsradar,
        'joinclassform': joinclassform
        # 'joinclassform': [joinclassform['klass'], 'hi']
    })
    
    

# Login and Register Function
SUBJECT_CHOICES = [
    ('', 'Subject '), ('Chinese', "Chinese"), ('English', "English"), ('Math', "Math"), ('Science', "Science"), ('Individuals and Societies', "Individuals and Societies"), ('Music',                                                                                                                                                                            "Music"), ('Drama', "Drama"), ('Art', "Art"), ('MYP Physical Education', "MYP Physical Education"), ('Design', "Design"), ('Computer Science', "Computer Science")
]


@ login_required(login_url='login')
@ allowed_users(allowed_roles=['students'])
def subjects(request):
    subjects = request.user.profile.subject_set.all()
    return render(request, 'dashboard/subjects.html', {'subjects': subjects})

def subject(request, sub):
    #Subject Main Graph
    monthgradecount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    avggrade = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    datasubject = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    datagrade = [0,0,0,0,0,0]
    datagrades = []
    srrs = []
    criterionavg = [0,0,0,0]
    labelsgrade = ["Criterion A", "Criterion B", "Criterion C",
                   "Criterion D", "Grade Average", "Subject Average"]
    labels = ["January", "Febuary", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    subject = request.user.profile.subject_set.all().get(subjectname=sub)
    # Calculate average for each month
    for grade in subject.grade_set.all():
        avg = (grade.criterionA+grade.criterionB +
                grade.criterionC+grade.criterionD)/4
        grade.avg = avg
        grade.save()
        month = grade.created.month
        monthgradecount[month-1] += 1
        avggrade[month-1] += avg
        datasubject[month-1] = avggrade[month-1]/monthgradecount[month-1]
    
    #Show most recent test with reflection
    for grade in subject.grade_set.all():
        datagrade[0] = grade.criterionA
        datagrade[1] = grade.criterionB
        datagrade[2] = grade.criterionC
        datagrade[3] = grade.criterionD
        datagrade[4] = float(grade.avg)
        datagrade[5] = float(grade.subject.subjectavg)
        datagrades.append(datagrade.copy())
        for srr in grade.srr_set.all():
            srrs.append(srr.srr)
    
    #Find worst criterion:
    num = 1
    for grade in subject.grade_set.all():
        criterionavg[0] = float((criterionavg[0]+float(grade.criterionA))/num)
        criterionavg[1] = float((criterionavg[1]+float(grade.criterionB))/num)
        criterionavg[2] = float((criterionavg[2]+float(grade.criterionC))/num)
        criterionavg[3] = float((criterionavg[3]+float(grade.criterionD))/num)
        num += 1
    return render(request, 'dashboard/subject.html', {'subject': subject, 'labels':labels, 'data':datasubject, 'datagrades':datagrades, 'labelsgrade':labelsgrade, 'srrs':srrs, 'criterionavg':criterionavg})


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
        if user is not None:
            auth_login(request, user)
            if user.groups.filter(name='students').exists():
                return redirect('index')
            elif user.groups.filter(name='teachers').exists():
                return redirect('teacherui')
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
def reflections(request):
    srrs = []
    bestdataradar = [0,0,0,0,0,0,0,0,0,0,0];
    worstdataradar = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    ATLs = ['Interaction','Language','Collaboration','Information Literacy','Media Literacy','Affective Skills','Organizational Skills','Reflection','Critical Thinking','Creative Thinking','Transfer']
    for srr in request.user.profile.srr_set.all():
        srrs.append(srr)
        for atl in ATLs:
            if(srr.bestatl == atl):
                bestdataradar[ATLs.index(atl)] += 1
            if(srr.worstatl == atl):
                worstdataradar[ATLs.index(atl)] += 1
    
    #Add Reflections
    reflectionform = SRRForm()
    if request.method == 'POST':
        #Add SRR
        reflectionform = SRRForm(request.POST)
        if reflectionform.is_valid():
            reflectionform.save()
    return render(request,  'dashboard/reflections.html', {'srrs': srrs, 'ATLs':ATLs, 'bestdataradar':bestdataradar, 'worstdataradar':worstdataradar, 'reflectionform':reflectionform} )


@ login_required(login_url='login')
def base(request):
    return render(request, 'dashboard/base.html', )


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
@ allowed_users(allowed_roles=['students'])
def editprofile(request):
    return render(request, 'dashboard/editprofile.html')


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