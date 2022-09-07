from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
# Create your views here.


def index(request):
    userinfo = User.objects.all()
    context = {'userinfo': userinfo}
    return render(request, 'dashboard/index.html', context)
