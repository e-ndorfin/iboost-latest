from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
# Create your views here.


def index(request):
    userinfo = User.objects.all()
    context = {'userinfo': userinfo}
    return render(request, 'dashboard/index.html', context)

def improvements(request):
    return render(request,  'dashboard/improvements1.html',{})

def base(request):
    return render(request, 'dashboard/base.html', )

def grades(request): 
    return render(request, 'dashboard/grades.html')

def improvements2(request):
    return render(request, 'dashboard/improvements2.html')

def improvements3(request):
    return render(request, 'dashboard/improvements3.html')

def profile(request):
    return render(request, 'dashboard/profile.html',)