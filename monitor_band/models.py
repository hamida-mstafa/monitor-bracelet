from django.db import models


class TempValues(models.Model):
    val = models.IntegerField(default=0)
    temperature=models.CharField(max_length=50, blank=True, null=True)
    time=models.DateTimeField(auto_now=True)