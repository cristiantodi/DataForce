from rest_framework.viewsets import ModelViewSet
from inventoryReport.models import inventorey
from inventoryReport.api.serializers import inventoreySerializer

class inventoreyApiViewSet(ModelViewSet):
    serializer_class = inventoreySerializer
    queryset = inventorey.objects.all()
    