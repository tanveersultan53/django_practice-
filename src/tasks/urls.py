"""Hanlde tasks app urls."""
from django.urls import path
from . import views

urlpatterns = [
    path("tasks/",views.TaskLabelView.as_view(), name="task_label")
]
