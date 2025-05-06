from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceStateViewSet

router = DefaultRouter()
router.register(r'device-states', DeviceStateViewSet, basename='device-state')

urlpatterns = [
    path('', include(router.urls)),
]