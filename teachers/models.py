from django.db import models
from students.models import Student
from jwt_auth.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Teacher(models.Model):
    User = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    image = models.CharField(max_length=500, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    student = models.ManyToManyField(
        Student, related_name='payments', blank=True)

    def __str__(self):
        return self.first_name


@receiver(post_save, sender=CustomUser)
def create_teacher(sender, instance, created, *args, **kwargs):
    if created and instance.isTeacher == True:
        print(sender.first_name)
        Teacher.objects.create(User=instance, first_name=instance.first_name, surname=instance.last_name, subject=instance.subject
                               )
        instance.save()
