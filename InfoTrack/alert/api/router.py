from rest_framework.routers import DefaultRouter
from alert.api.views import alertEventApiView

router_alertEvent = DefaultRouter()

router_alertEvent.register(prefix='alertEvent', basename='alertEvent', viewset=alertEventApiView)