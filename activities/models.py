from django.db import models
from users.models import Department


class Activity(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    place = models.TextField()
    date = models.DateTimeField()
    duration = models.DurationField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class ActivityFiles(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    path = models.FileField()
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)
