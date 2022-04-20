from django.db import models
from parents.models import Parent
from basket.models import Basket
from django.core.validators import MinValueValidator
# Create your models here.


class Payment(models.Model):
    amount = models.IntegerField(
        validators=[MinValueValidator(0)])
    parent = models.ForeignKey(
        Parent, related_name='payments',  on_delete=models.CASCADE, null=True)
    basket = models.ForeignKey(
        Basket, related_name='payments',  on_delete=models.CASCADE, null=True)

    def __int__(self):
        return self.student
