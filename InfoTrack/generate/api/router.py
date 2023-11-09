from rest_framework.routers import DefaultRouter
from generate.api.views import infomationGenerateApiView

router_infomationGenerate = DefaultRouter()

router_infomationGenerate.register(prefix='infomationGenerate', basename='infomationGenerate', viewset=infomationGenerateApiView)