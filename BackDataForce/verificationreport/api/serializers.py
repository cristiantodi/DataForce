from rest_framework import serializers
from verificationreport.models import android, iphone

class androidSerializer(serializers.ModelSerializer):
    class Meta :
        model   = android
        fields  =  [
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
        
class iphoneSerializer(serializers.ModelSerializer):
    class Meta :
        model   = iphone
        fields  =  [
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