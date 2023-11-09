from django.db import models

# Create your models here.

class infomationGenerate(models.Model):
    owner           =   models.CharField(max_length=200, blank=True, null=True)
    documentName    =   models.CharField(max_length=200, blank=True, null=True)
    documentAuthor  =   models.CharField(max_length=200, blank=True, null=True)
    job             =   models.CharField(max_length=200, blank=True, null=True)
    docType         =   models.CharField(max_length=200, blank=True, null=True)
