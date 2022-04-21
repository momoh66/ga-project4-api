from dataclasses import field
from rest_framework import serializers
from students.serializers import StudentPopulatedSerializerWithBaskets
from messaging.serializers import MessagingSerializer
from .models import Parent


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ('__all__')


class ParentPopulatedSerializer(ParentSerializer):
    students = StudentPopulatedSerializerWithBaskets(many=True)
    messages =MessagingSerializer(many=True)
