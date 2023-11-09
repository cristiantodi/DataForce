from rest_framework.viewsets import ModelViewSet
from alert.models import alertEvent
from alert.api.serializers import alertEventSerializer

class alertEventApiView(ModelViewSet):
    serializer_class = alertEventSerializer
    queryset = alertEvent.objects.all()
    
