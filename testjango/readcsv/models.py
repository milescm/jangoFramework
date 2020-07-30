from django.db import models
from django.conf import settings


class CsvData(models.Model):
    objects = models.Manager()
    realtime_timestamp = models.CharField(max_length=20)
    monolithic_timestamp = models.CharField(max_length=20)
    utc = models.CharField(max_length=20)
    master_offset = models.IntegerField()
    frequency = models.IntegerField()
    path_delay = models.IntegerField()

    
