from rest_framework.routers import DefaultRouter
from verificationreport.api.views import androidApiViewSer, iphoneApiViewSer

router_verificationreport = DefaultRouter()

router_verificationreport.register(prefix='android', basename='android', viewset=androidApiViewSer)
router_verificationreport.register(prefix=' iphone', basename=' iphone', viewset=iphoneApiViewSer)