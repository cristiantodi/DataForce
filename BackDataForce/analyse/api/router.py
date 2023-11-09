from rest_framework.routers import DefaultRouter
from analyse.api.views import analizysApiViewSer

router_analyse = DefaultRouter()

router_analyse.register(prefix='analyse', basename='analyse', viewset=analizysApiViewSer)