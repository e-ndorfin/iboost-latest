from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
# Create your views here.


def index(request):
    usernames = Username.objects.all()
    context = {'usernames': usernames}
    return render(request, 'dashboard/index.html', context)
