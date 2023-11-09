from rest_framework import serializers
from configuration.models import alertSetting

class alertSettingSerializer(serializers.ModelSerializer):
    class Meta :
        model   = alertSetting
        fields  =  [
                    "id",
                    "filters",
                    "sensor",
                    "option",
                    ]