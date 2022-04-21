from django.db import models
from jwt_auth.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.

# User = get_user_model()


class Parent(models.Model):
    User = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    image = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.first_name


@receiver(post_save, sender=CustomUser)
def create_parent(sender, instance, created, *args, **kwargs):
    if created and instance.isParent == True:
        Parent.objects.create(User=instance, first_name=instance.first_name, surname=instance.last_name,  image=instance.image)
        instance.save()


