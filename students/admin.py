from django.contrib import admin
from .models import *
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'surname',
                    'date_of_birth', 'sex', 'admission_date', 'year_group', 'paid')


admin.site.register(Student, StudentAdmin)
