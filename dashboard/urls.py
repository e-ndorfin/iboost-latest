from django.urls import path
from . import views
from .views import line_chart, line_chart_json

urlpatterns = [
    path('base/', views.base, name="base"),
    path('index/', views.index, name="index"),

    path('improvements/', views.improvements, name="improvements"),
    path('grades/', views.grades, name='grades'),
    path('improvements2/', views.improvements2, name='improvements2'),
    path('improvements3/', views.improvements3, name='improvements3'),
    path('profile/', views.profile, name='profile'),
    path('testing/', views.testing, name='testing'),
    path('chart', line_chart, name='line_chart'),
    path('chartJSON', line_chart_json, name='line_chart_json'),
    path('chineseg/', views.chineseg, name="chineseg"),
    path('register/', views.registerPage, name="register"),
    path('modaltest/', views.modaltest, name="modaltest"),
    path('radialtest/', views.radialtest, name="radialtest"),
    path('accountcreation/', views.accountcreation, name="accountcreation"), 
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name="logout"),
]
