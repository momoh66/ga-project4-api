from django.shortcuts import render
from rest_framework.generics import *
from .models import Basket

from .serializers import *
# Create your views here.


class BasketList(ListCreateAPIView):

    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


class BasketRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):

    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
