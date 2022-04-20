from dataclasses import field
from rest_framework import serializers
from basket.serializers import BasketSerializerForDetailedStudentView
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('__all__')


class StudentPopulatedSerializerWithBaskets(StudentSerializer):
    baskets = BasketSerializerForDetailedStudentView(many=True)
