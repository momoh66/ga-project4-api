from django.db import models
from django.contrib.auth import get_user_model
from parents.models import Parent
User = get_user_model()
# Create your models here.


class Message(models.Model):
    text = models.CharField(max_length=300)
    owner = models.ForeignKey(
        User, related_name='messages', on_delete=models.PROTECT)
    recipient_parent = models.ForeignKey(
        Parent, related_name='messages', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
