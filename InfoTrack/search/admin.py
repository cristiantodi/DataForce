from django.contrib import admin
from search.models import informationSearch

# Register your models here.

@admin.register(informationSearch)
class informationSearchAdmin(admin.ModelAdmin):
    list_display = [
                    "id",
                    "sel",
                    "date",
                    "ownerauthor",
                    "documentName",
                    "docType",
                    "ip",
                    "netName",
                    "countryName",
                    "countryCode",
                    "gmt",
                    "regioncity",
                    "isp",
                    "os",
                    "plataform",
                    "suite",
                ] 