from rest_framework.routers import DefaultRouter
from configuration.api.views import alertSettingApiView

router_alertSetting = DefaultRouter()

router_alertSetting.register(prefix='alertSetting', basename='alertSetting', viewset=alertSettingApiView)