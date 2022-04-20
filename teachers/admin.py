from django.contrib import admin
from .models import *
# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'subject')


admin.site.register(Teacher, TeacherAdmin)
