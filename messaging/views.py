from django.shortcuts import render
from rest_framework.generics import *
from .models import Message

from .serializers import *
# Create your views here.


class MessagesList(ListCreateAPIView):

    queryset = Message.objects.all()
    serializer_class = MessagingSerializer


class MessagesRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):

    queryset = Message.objects.all()
    serializer_class = MessagingSerializer
