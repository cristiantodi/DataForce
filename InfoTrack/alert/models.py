from django.db import models

# Create your models here.

class alertEvent(models.Model):
    owner       =   models.CharField(max_length=200, blank=True, null=True)
    author      =   models.CharField(max_length=200, blank=True, null=True)
    document    =   models.CharField(max_length=200, blank=True, null=True)
    docType     =   models.CharField(max_length=200, blank=True, null=True)
    alert       =   models.CharField(max_length=200, blank=True, null=True)
    opened      =   models.CharField(max_length=200, blank=True, null=True)
    country     =   models.CharField(max_length=200, blank=True, null=True)
    regioncity  =   models.CharField(max_length=200, blank=True, null=True)
    ip          =   models.CharField(max_length=200, blank=True, null=True)