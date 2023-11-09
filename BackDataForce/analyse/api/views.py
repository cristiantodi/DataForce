from rest_framework.viewsets import ModelViewSet
from analyse.models import analizys
from analyse.api.serializers import analizysSerializer

class analizysApiViewSer(ModelViewSet):
    serializer_class = analizysSerializer
    queryset = analizys.objects.all()
    
