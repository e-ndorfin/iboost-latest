from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

from .models import *
# Create your views here.

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    def get_providers(self):
        """Return names of datasets."""
        return ["English", "Chinese", "Chemistry"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[0,0,0,4,6,5,7,4,4,4,6,7],
            [0,0,0,4,5,6,7,4,7,4,7,8,8],
            [0,0,0,5,7,4,6,7,8,8,8,8,8]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()  


def index(request):
    userinfo = User.objects.all()
    context = {'userinfo': userinfo}
    return render(request, 'dashboard/index.html', context)


def improvements(request):
    return render(request,  'dashboard/improvements1.html', {})


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


def login(request):
    return render(request, 'dashboard/login.html')


def testing(request):
    grades = Grade.objects.all()
    subjectname = Subject.objects.all()
    return render(request, 'dashboard/testing.html', {'grades': grades, 'subjectname': subjectname},)

