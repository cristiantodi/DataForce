from django.db import models

# Create your models here.

class android(models.Model):
    uniqueCode      =   models.CharField(max_length=200, blank=True, null=True) 
    ReportDate      =   models.DateField(blank=True, null=True)
    platform        =   models.CharField(max_length=200, blank=True, null=True)
    uniqueDeviceId  =   models.CharField(max_length=200, blank=True, null=True)
    productName     =   models.CharField(max_length=200, blank=True, null=True)
    brand           =   models.CharField(max_length=200, blank=True, null=True)
    maker           =   models.CharField(max_length=200, blank=True, null=True)
    productCode     =   models.CharField(max_length=200, blank=True, null=True)
    radioSerial     =   models.CharField(max_length=200, blank=True, null=True)
    version_so      =   models.CharField(max_length=200, blank=True, null=True)
    model_id        =   models.CharField(max_length=200, blank=True, null=True)
    computerMD      =   models.CharField(max_length=200, blank=True, null=True)
    conputerSHA     =   models.CharField(max_length=200, blank=True, null=True) 

class iphone(models.Model):
    uniqueReportIdentifier  =   models.CharField(max_length=200, blank=True, null=True) 
    ReportDate      =   models.DateField(blank=True, null=True)
    platform        =   models.CharField(max_length=200, blank=True, null=True)
    uniqueCode      =   models.CharField(max_length=200, blank=True, null=True)
    deviceFamily    =   models.CharField(max_length=200, blank=True, null=True)
    productName     =   models.CharField(max_length=200, blank=True, null=True)
    model           =   models.CharField(max_length=200, blank=True, null=True)
    version_so      =   models.CharField(max_length=200, blank=True, null=True)
    modelNumber     =   models.CharField(max_length=200, blank=True, null=True)
    serialNumber    =   models.CharField(max_length=200, blank=True, null=True)
    modelHardware   =   models.CharField(max_length=200, blank=True, null=True)
    serialDataBase  =   models.CharField(max_length=200, blank=True, null=True)
    imei            =   models.CharField(max_length=200, blank=True, null=True)
    codeCountry     =   models.CharField(max_length=200, blank=True, null=True)
    codeOperator    =   models.CharField(max_length=200, blank=True, null=True)
    addressBluetoot =   models.CharField(max_length=200, blank=True, null=True)
    addressEthernet =   models.CharField(max_length=200, blank=True, null=True)
    addressWife     =   models.CharField(max_length=200, blank=True, null=True)
    computerMD      =   models.CharField(max_length=200, blank=True, null=True)
    conputerSHA     =   models.CharField(max_length=200, blank=True, null=True) 
    
