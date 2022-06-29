from http import server
from django.shortcuts import render
from rest_framework import generics,response

from tasks.models import TaskLable

from .serializers import SerializerTaskLabel


# Create your views here.

class TaskLabelView(generics.GenericAPIView):
    serializer_class = SerializerTaskLabel

    def get_queryset(self):
        return TaskLable.objects.all()

    def get(self, request, *args, **kwargs):
        serialized_data = SerializerTaskLabel(TaskLable.objects.all(),many=True)
        return response.Response(data=serialized_data.data)
    
    def post(self, request, *args, **kwargs):
        serialized_data = self.get_serializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return response.Response(data=serialized_data.data)
        return response.Response(data={"Message":"welcome!"})
