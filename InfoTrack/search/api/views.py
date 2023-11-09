from rest_framework.viewsets import ModelViewSet
from search.models import informationSearch
from search.api.serializers import informationSearchSerializer

class informationSearchApiView(ModelViewSet):
    serializer_class = informationSearchSerializer
    queryset = informationSearch.objects.all()
    
