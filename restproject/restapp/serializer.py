from rest_framework import serializers
from restapp.models import Employee

class EmployeeSerilalizer(serializers.Serializer):
    name=serializers.CharField(max_length=30)
    no=serializers.IntegerField()
    role=serializers.CharField(max_length=30)
    salary=serializers.FloatField()
    location=serializers.CharField(max_length=30)
