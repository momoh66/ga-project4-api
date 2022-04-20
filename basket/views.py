from django.shortcuts import render
from rest_framework.generics import *
from .models import Basket
from rest_framework.permissions import IsAuthenticated
from .serializers import *
# Create your views here.


class BasketList(ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


class BasketRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
