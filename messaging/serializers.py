from dataclasses import field
from rest_framework import serializers
from .models import Message


class MessagingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('__all__')



