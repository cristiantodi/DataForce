from rest_framework.routers import DefaultRouter
from report.api.views import reportApiViewSet

router_report = DefaultRouter()

router_report.register(prefix='report', basename='report', viewset=reportApiViewSet)