from email.mime import image
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from parents.models import Parent
# Create your models here.


class Student(models.Model):

    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField(max_length=6)
    admission_date = models.DateField(auto_now=True)
    image = models.CharField(max_length=500)
    year_group = models.IntegerField(
        validators=[MinValueValidator(7), MaxValueValidator(13)])
    parent = models.ManyToManyField(
        Parent, related_name='students')
    sex = models.CharField(max_length=6)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.surname} - Year: {self.year_group}'
