from django.contrib import admin
from verificationreport.models import android, iphone

# Register your models here.

@admin.register(android)
class androidAdmin(admin.ModelAdmin):
    list_display = [
                    "id",
                    "uniqueCode",
                    "ReportDate",
                    "platform",
                    "uniqueDeviceId",
                    "productName",
                    "brand",
                    "maker",
                    "productCode",
                    "radioSerial",
                    "version_so",
                    "model_id",
                    "computerMD",
                    "conputerSHA",
    ]




@admin.register(iphone)
class iphoneAdmin(admin.ModelAdmin):
    list_display = [
                    "id",
                    "uniqueReportIdentifier",
                    "ReportDate",
                    "platform",
                    "uniqueCode",
                    "deviceFamily",
                    "productName",
                    "model",
                    "version_so",
                    "modelNumber",
                    "serialNumber",
                    "modelHardware",
                    "serialDataBase",
                    "imei",
                    "codeCountry",
                    "codeOperator",
                    "addressBluetoot",
                    "addressEthernet",
                    "addressWife",
                    "computerMD",
                    "conputerSHA",
    ]
