from django.contrib import admin

# Register your models here.
from .models import *
from dashboard.models import *

admin.site.register(Teacher)
admin.site.register(Klass)
admin.site.register(Student)