from rest_framework import serializers
from .models import Device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'type', 'model', 'manufacturer', 'firmware_version',
                 'ip_address', 'mac_address', 'is_online', 'metadata', 'user', 
                 'room', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']