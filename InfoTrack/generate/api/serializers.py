from rest_framework import serializers
from generate.models import infomationGenerate

class infomationGenerateSerializer(serializers.ModelSerializer):
    class Meta :
        model   = infomationGenerate
        fields  =  [
                    "id",
                    "owner",
                    "documentName",
                    "documentAuthor",
                    "job",
                    "docType",
                    ]