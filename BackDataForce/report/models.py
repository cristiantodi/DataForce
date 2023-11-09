from django.db import models
from users.models import User

# Create your models here.

class reports(models.Model):
    uniqueCode      =   models.CharField(max_length=200, blank=True, null=True) 
    generationDate  =   models.DateTimeField(auto_now_add=True) #models.DateField(blank=True, null=True)
    user            =   models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING)
    uniqueReportIdentifier  =   models.CharField(max_length=200, blank=True, null=True) 
    ReportDate      =   models.DateField(blank=True, null=True)
    architecture    =   models.IntegerField(blank=True, null=True)
    platform        =   models.IntegerField(blank=True, null=True)
    uniqueDeviceId  =   models.CharField(max_length=200, blank=True, null=True)
    productName     =   models.CharField(max_length=200, blank=True, null=True)
    maker           =   models.CharField(max_length=200, blank=True, null=True)
    model           =   models.CharField(max_length=200, blank=True, null=True)
    productCode     =   models.CharField(max_length=200, blank=True, null=True)
    serial_so       =   models.CharField(max_length=200, blank=True, null=True)
    code_so         =   models.CharField(max_length=200, blank=True, null=True)
    model_id        =   models.CharField(max_length=200, blank=True, null=True)
    computerMD      =   models.CharField(max_length=200, blank=True, null=True)
    conputerSHA     =   models.CharField(max_length=200, blank=True, null=True) 