from django.urls import path
from . import views

urlpatterns = [
    # path('base/', views.base, name="base"),
    # path('index/', views.index, name="index")
    path('teacherui/', views.teacherui, name="teacherui"),
    path('teacherclass/<str:klass>', views.teacherclass, name='teacherclass'),
    path('teacheraccountcreation/', views.teacheraccountcreation, name='teacheraccountcreation'),
]
