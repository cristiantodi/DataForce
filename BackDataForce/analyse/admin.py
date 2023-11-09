from django.contrib import admin
from analyse.models import analizys

# Register your models here.

@admin.register (analizys)
class analyseAdmin(admin.ModelAdmin):
    list_display = [
                    "id",
                    "uniqueCode",  
                    "user",
                    "initiated",
                    "termination", 
                    "result",
                    "type",
    ]
    