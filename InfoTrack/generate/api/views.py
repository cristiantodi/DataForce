from rest_framework.viewsets import ModelViewSet
from generate.models import infomationGenerate
from generate.api.serializers import infomationGenerateSerializer

class infomationGenerateApiView(ModelViewSet):
    serializer_class = infomationGenerateSerializer
    queryset = infomationGenerate.objects.all()
    
