from rest_framework import serializers
from .models import DeviceState

class DeviceStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceState
        fields = ['id', 'device', 'state_data', 'created_at']
        read_only_fields = ['id', 'created_at']