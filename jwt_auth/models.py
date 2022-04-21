
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class CustomUser(AbstractUser):

    image = models.CharField(max_length=200)
    isParent = models.BooleanField(default=False)
    isTeacher = models.BooleanField(default=False)
    isStudent = models.BooleanField(default=False)
    date_of_birth = models.DateField(max_length=6, null=True)
    admission_date = models.DateField(auto_now=True)
    image = models.CharField(max_length=500)
    year_group = models.IntegerField(
        validators=[MinValueValidator(7), MaxValueValidator(13)], null=True)
    sex = models.CharField(max_length=6, null=True)
    paid = models.BooleanField(default=False)
    subject = models.CharField(max_length=100, blank=True, null=True)
