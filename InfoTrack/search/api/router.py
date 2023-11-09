from rest_framework.routers import DefaultRouter
from search.api.views import informationSearchApiView

router_informationSearch = DefaultRouter()

router_informationSearch.register(prefix='informationSearch', basename='informationSearch', viewset=informationSearchApiView)