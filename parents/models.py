from django.db import models

# Create your models here.


class Parent(models.Model):

    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    image = models.CharField(max_length=100, blank=True)
   
    def __str__(self):
        return self.first_name
