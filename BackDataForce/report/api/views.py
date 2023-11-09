from rest_framework.viewsets import ModelViewSet
from report.models import reports
from report.api.serializers import reportSerializer

class reportApiViewSet(ModelViewSet):
    serializer_class = reportSerializer
    queryset = reports.objects.all()
