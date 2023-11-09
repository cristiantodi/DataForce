from rest_framework import serializers
from search.models import informationSearch

class informationSearchSerializer(serializers.ModelSerializer):
    class Meta :
        model   = informationSearch
        fields  =  [
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