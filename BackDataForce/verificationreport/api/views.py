from rest_framework.viewsets import ModelViewSet
from verificationreport.models import android, iphone
from verificationreport.api.serializers import androidSerializer, iphoneSerializer

class androidApiViewSer(ModelViewSet):
    serializer_class = androidSerializer
    queryset = android.objects.all()
    
class iphoneApiViewSer(ModelViewSet):
    serializer_class = iphoneSerializer
    queryset = iphone.objects.all()