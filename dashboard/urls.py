from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('improvements/', views.improvements, name="improvements"),
    path('base/', views.base, name="base"),
    path('grades/', views.grades, name='grades'),
    path('improvements2/', views.improvements2, name='improvements2'),
    path('improvements3/', views.improvements3, name='improvements3'),
    path('profile/', views.profile, name='profile'),
]
