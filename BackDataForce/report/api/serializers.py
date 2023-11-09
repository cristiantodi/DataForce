from rest_framework import serializers
from report.models import reports

class reportSerializer(serializers.ModelSerializer):
    class Meta:
        model   = reports
        fields  = [
                    "id",
                    "uniqueCode",
                    "generationDate",
                    "user",
                    "uniqueReportIdentifier",
                    "ReportDate",
                    "architecture",
                    "platform",
                    "uniqueDeviceId",
                    "productName",
                    "maker",
                    "model",
                    "productCode",
                    "serial_so",
                    "code_so",
                    "model_id",
                    "computerMD",
                    "conputerSHA",
                ]