from email.mime import image
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from parents.models import Parent
from jwt_auth.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Student(models.Model):
    User = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField(max_length=6, null=True)
    admission_date = models.DateField(auto_now=True)
    image = models.CharField(max_length=500)
    year_group = models.IntegerField(
        validators=[MinValueValidator(7), MaxValueValidator(13)],null=True)
    parent = models.ManyToManyField(
        Parent, related_name='students')
    sex = models.CharField(max_length=6, null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.surname} - Year: {self.year_group}'


@receiver(post_save, sender=CustomUser)
def create_student(sender, instance, created, *args, **kwargs):
    if created and instance.isStudent == True:
        print(sender.date_of_birth)
        Student.objects.create(User=instance, first_name=instance.first_name, surname=instance.last_name,
                                  date_of_birth=instance.date_of_birth, sex=instance.sex, year_group=instance.year_group
                               )
        instance.save()
