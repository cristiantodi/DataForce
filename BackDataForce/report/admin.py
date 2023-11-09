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