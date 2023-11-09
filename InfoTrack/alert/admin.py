from django.contrib import admin
from alert.models import alertEvent

# Register your models here.

@admin.register(alertEvent)
class alertEventAdmin(admin.ModelAdmin):
    list_display = [
                    "id",
                    "owner",
                    "author",
                    "document",
                    "docType",
                    "alert",
                    "opened",
                    "country",
                    "regioncity",
                    "ip",
                ] 