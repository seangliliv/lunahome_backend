from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/', include('users.urls')),
    path('api/', include('rooms.urls')),
    path('api/', include('devices.urls')),
    path('api/', include('device_states.urls')),
    path('api/', include('automations.urls')),
]