from rest_framework.routers import DefaultRouter
from inventoryReport.api.views import inventoreyApiViewSet

router_inventory = DefaultRouter()

router_inventory.register(prefix='inventory', basename='inventory', viewset=inventoreyApiViewSet)