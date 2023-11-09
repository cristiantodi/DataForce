from django.db import models

# Create your models here.

class alertSetting(models.Model):
    filters =   models.CharField(max_length=200, blank=True, null=True)
    sensor  =   models.CharField(max_length=200, blank=True, null=True)
    option  =   models.CharField(max_length=200, blank=True, null=True)
