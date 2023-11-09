"""
URL configuration for InfoTrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from search.api.router import router_informationSearch
from generate.api.router import router_infomationGenerate
from configuration.api.router import router_alertSetting
from alert.api.router import router_alertEvent

# from user.api.router import user

schema_view = get_schema_view(
   openapi.Info(
        title="Info Track API",
        default_version='v1',
        description="Documentacion de la API",
        terms_of_service="",
        contact=openapi.Contact(email="dev01@dataenforce.com"),
        license=openapi.License(name="BSD License"),
   ),
    public=True,
#    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('user.api.router')),
    path('api/', include(router_informationSearch.urls)),
    path('api/', include(router_infomationGenerate.urls)),
    path('api/', include(router_alertSetting.urls)),
    path('api/', include(router_alertEvent.urls)),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
