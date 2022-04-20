
from django.db import models
from django.contrib.auth.models import AbstractUser
from parents.models import Parent
from teachers.models import Teacher
from students.models import Student
# Create your models here.


class CustomUser(AbstractUser):

    image = models.CharField(max_length=200)
    parent = models.ForeignKey(
        Parent, related_name='CustomUser', on_delete=models.PROTECT, blank=True, null=True)
    teacher = models.ForeignKey(
        Teacher, related_name='CustomUser', on_delete=models.PROTECT, blank=True, null=True)
    student = models.ForeignKey(
        Student, related_name='CustomUser', on_delete=models.PROTECT, blank=True, null=True)
    isParent = models.BooleanField(default=False)
    isTeacher = models.BooleanField(default=False)
    isStudent = models.BooleanField(default=False)
