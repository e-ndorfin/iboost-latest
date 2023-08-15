from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base, name="base"),
    path('index/', views.index, name="index")
]
