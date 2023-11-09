from django.contrib import admin
from report.models import reports

# Register your models here.

@admin.register(reports)
class reportsAdmin(admin.ModelAdmin):
    list_display = [
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