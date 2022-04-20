from dataclasses import field
from rest_framework import serializers
from students.serializers import StudentSerializer
from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('__all__')


