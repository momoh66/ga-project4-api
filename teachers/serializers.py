from dataclasses import field
from rest_framework import serializers
from messaging.serializers import MessagingSerializer
from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('__all__')


class TeacherPopulatedSerializerWithMessages(TeacherSerializer):
    messages = MessagingSerializer(many=True)
