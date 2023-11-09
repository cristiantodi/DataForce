from django.contrib import admin
from inventoryReport.models import inventorey

# Register your models here.

@admin.register(inventorey)
class inventoreyAdmin(admin.ModelAdmin):
    list_display = [
                    "id",
                    "uniqueCode",
                    "generationDate",
                    "user",
                    "type",
                    "model_id",
                    "archive",
                ] 