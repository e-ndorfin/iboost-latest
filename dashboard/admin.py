from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Grade)
admin.site.register(Subject)
admin.site.register(Profile)
admin.site.register(SRR)
