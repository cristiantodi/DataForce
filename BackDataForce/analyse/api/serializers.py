from rest_framework import serializers
from analyse.models import analizys

class analizysSerializer(serializers.ModelSerializer):
    class Meta :
        model   = analizys
        fields  =  [
                    "id",
                    "uniqueCode",  
                    "user",
                    "initiated",
                    "termination", 
                    "result",
                    "type",
                    ]