from django.shortcuts import render
from rest_framework.generics import *

from .models import Parent
from .serializers import *
# Create your views here.


class ParentList(ListCreateAPIView):

    queryset = Parent.objects.all()
    serializer_class = ParentSerializer



class ParentDetailedView(RetrieveAPIView):

    queryset = Parent.objects.all()
    serializer_class = ParentPopulatedSerializer


class ParentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):

    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
