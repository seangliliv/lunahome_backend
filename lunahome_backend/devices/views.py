from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Device
from .serializers import DeviceSerializer
from device_states.models import DeviceState
from device_states.serializers import DeviceStateSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Device.objects.filter(user=self.request.user)
        room_id = self.request.query_params.get('room', None)
        if room_id:
            queryset = queryset.filter(room__id=room_id)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['get'])
    def states(self, request, pk=None):
        device = self.get_object()
        states = DeviceState.objects.filter(device=device)[:10]
        serializer = DeviceStateSerializer(states, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def current_state(self, request, pk=None):
        device = self.get_object()
        try:
            state = DeviceState.objects.filter(device=device).latest('created_at')
            serializer = DeviceStateSerializer(state)
            return Response(serializer.data)
        except DeviceState.DoesNotExist:
            return Response({"detail": "No state recorded for this device"}, status=404)