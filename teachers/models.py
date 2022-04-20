from django.db import models
from students.models import Student
# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    subject = models.CharField(max_length=100)
    student = models.ManyToManyField(
        Student, related_name='payments')

    def __str__(self):
        return self.first_name
