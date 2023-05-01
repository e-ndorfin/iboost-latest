from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base, name="base"),
    path('index/', views.index, name="index"),

    path('improvements/', views.improvements, name="improvements"),
    path('grades/', views.grades, name='grades'),
    path('profile/', views.profile, name='profile'),
    path('testing/', views.testing, name='testing'),
    path('chineseg/', views.chineseg, name="chineseg"),
    path('register/', views.registerPage, name="register"),
    path('modaltest/', views.modaltest, name="modaltest"),
    path('radialtest/', views.radialtest, name="radialtest"),
    path('accountcreation/', views.accountcreation, name="accountcreation"), 
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name="logout"),
    # path('mainchart/', views.main_chart, name="main_chart"),
    path('interviewarchive/', views.interviewarchive, name="interviewarchive"),
    path('editprofile/', views.editprofile, name="editprofile"),
]
