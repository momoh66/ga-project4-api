from os import name
from django.db import models
from students.models import Student
from django.core.validators import MinValueValidator
# Create your models here.


class Basket(models.Model):
    name = models.CharField(max_length=100, null=True)
    amount = models.IntegerField(
        validators=[MinValueValidator(0)])
    student = models.ManyToManyField(
        Student, related_name='baskets', blank=True)

    def __str__(self):
        return  f'Bakset Id: {self.id}'
