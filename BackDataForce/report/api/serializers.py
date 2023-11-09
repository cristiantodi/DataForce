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
                    "ProductName",
                    "maker",
                    "model",
                    "ProductCode",
                    "serial_so",
                    "code_so",
                    "model_id",
                    "computerHash",
                    "hashTeam"
                ]