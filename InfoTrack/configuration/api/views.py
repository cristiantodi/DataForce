from rest_framework.viewsets import ModelViewSet
from configuration.models import alertSetting
from configuration.api.serializers import alertSettingSerializer

class alertSettingApiView(ModelViewSet):
    serializer_class = alertSettingSerializer
    queryset = alertSetting.objects.all()
    
