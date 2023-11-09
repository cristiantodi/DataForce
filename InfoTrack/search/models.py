from django.db import models

# Create your models here.

class informationSearch(models.Model):
    sel         =   models.BooleanField(default=False)
    date        =   models.DateField(blank=True, null=True)
    ownerauthor =   models.CharField(max_length=200, blank=True, null=True)
    documentName =   models.CharField(max_length=200, blank=True, null=True)
    docType     =   models.CharField(max_length=200, blank=True, null=True) 
    ip          =   models.CharField(max_length=200, blank=True, null=True)
    netName     =   models.CharField(max_length=200, blank=True, null=True)
    countryName =   models.CharField(max_length=200, blank=True, null=True)
    countryCode =   models.CharField(max_length=200, blank=True, null=True)
    gmt         =   models.CharField(max_length=200, blank=True, null=True)
    regioncity  =   models.CharField(max_length=200, blank=True, null=True)
    isp         =   models.CharField(max_length=200, blank=True, null=True)
    os          =   models.CharField(max_length=200, blank=True, null=True)
    plataform   =   models.CharField(max_length=200, blank=True, null=True)
    suite       =   models.CharField(max_length=200, blank=True, null=True)
   
