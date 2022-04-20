from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from .models import Parent
from .serializers import *
# Create your views here.


class ParentList(ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class ParentWithStudentView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Parent.objects.all()
    serializer_class = ParentPopulatedSerializer


class ParentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
