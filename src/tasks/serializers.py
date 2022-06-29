from dataclasses import field
from rest_framework import serializers
from .models import TaskLable

class SerializerTaskLabel(serializers.ModelSerializer):
    class Meta:
        model = TaskLable
        fields = ("name","is_active")