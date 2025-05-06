from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import DeviceState
from .serializers import DeviceStateSerializer

class DeviceStateViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceStateSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return DeviceState.objects.filter(device__user=self.request.user)
    
    def create(self, request):
        # Check if user owns the device
        device_id = request.data.get('device')
        if not request.user.devices.filter(id=device_id).exists():
            return Response({"detail": "Device not found or not owned by user"}, 
                          status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)