from django.contrib import admin
from generate.models import infomationGenerate

# Register your models here.

@admin.register(infomationGenerate)
class infomationGenerateAdmin(admin.ModelAdmin):
    list_display = [
                    "id",
                    "owner",
                    "documentName",
                    "documentAuthor",
                    "job",
                    "docType",
                ] 