from django.contrib import admin

from quickstart.models import Student
from .views import *
# Register your models here.
admin.site.register(Student)