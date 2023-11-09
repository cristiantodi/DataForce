from rest_framework import serializers
from alert.models import alertEvent

class alertEventSerializer(serializers.ModelSerializer):
    class Meta :
        model   = alertEvent
        fields  =  [
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