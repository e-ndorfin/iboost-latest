from django.urls import path
from . import views

urlpatterns = [
    # path('base/', views.base, name="base"),
    # path('index/', views.index, name="index")
<<<<<<< HEAD
    path('teacherui/', views.teacherui, name="teacherui"),
    path('teacherclass/', views.teacherclass, name='teacherclass'),
=======
    path('teacherui', views.teacherui, name="teacherui")
>>>>>>> 939225835867056dea5b60e3945c388829677dd8
    
]
