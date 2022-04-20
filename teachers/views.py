from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Teacher
from .serializers import *
# Create your views here.


class TeacherList(ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
