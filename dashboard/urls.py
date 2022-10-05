from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('improvements/', views.improvements, name="improvements"),
    path('base/', views.base, name="base"),
]
