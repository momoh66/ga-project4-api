from django.shortcuts import render
from rest_framework.generics import *
from .models import Message
from rest_framework.permissions import IsAuthenticated
from .serializers import *
# Create your views here.


class MessagesList(ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Message.objects.all()
    serializer_class = MessagingSerializer


class MessagesRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Message.objects.all()
    serializer_class = MessagingSerializer
