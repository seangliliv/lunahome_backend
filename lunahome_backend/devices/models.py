from django.db import models
import uuid
from users.models import User
from rooms.models import Room

class Device(models.Model):
    DEVICE_TYPES = [
        ('light', 'Light'),
        ('fan', 'Fan'),
        ('thermostat', 'Thermostat'),
        ('lock', 'Lock'),
        ('camera', 'Camera'),
        ('speaker', 'Speaker'),
        ('other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=DEVICE_TYPES)
    model = models.CharField(max_length=255, blank=True, null=True)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    firmware_version = models.CharField(max_length=50, blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    mac_address = models.CharField(max_length=17, blank=True, null=True)
    is_online = models.BooleanField(default=True)
    metadata = models.JSONField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devices')
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True, related_name='devices')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.type})"