from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView

from .models import Teacher
from .serializers import *
# Create your views here.


class TeacherList(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherWithMessagesView(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherPopulatedSerializerWithMessages

class TeacherRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
