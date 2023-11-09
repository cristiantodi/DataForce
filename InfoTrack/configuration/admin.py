from django.contrib import admin
from configuration.models import alertSetting

# Register your models here.

@admin.register(alertSetting)
class alertSettingAdmin(admin.ModelAdmin):
    list_display = [
                    "id",
                    "filters",
                    "sensor",
                    "option",
                ] 