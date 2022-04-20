from django.contrib import admin
from .models import *
# Register your models here.


class ParentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'surname')


admin.site.register(Parent, ParentAdmin)
