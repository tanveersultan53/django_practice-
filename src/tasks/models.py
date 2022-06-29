from django.db import models
from django.utils import timezone
# Create your models here.


class TaskLable(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label ="tasks"
        db_table = "task_label"
        verbose_name = "Task Label"
        verbose_name_plural = "Task Labels"

# class DailyDayTask(models.Model):
#     task_name

