from django.shortcuts import render
from rest_framework import status

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import Student
from .serializers import *
# Create your views here.


class StudentList(ListCreateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentWithBasketView(RetrieveAPIView):
   
    queryset = Student.objects.all()
    serializer_class = StudentPopulatedSerializerWithBaskets


class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
