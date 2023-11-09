from rest_framework import serializers

from inventoryReport.models import inventorey

class inventoreySerializer(serializers.ModelSerializer):
    class Meta:
        model   = inventorey
        fields  = [
                    "id",
                    "uniqueCode",
                    "generationDate",
                    "user",
                    "type",
                    "model_id",
                    "archive",
                ] 