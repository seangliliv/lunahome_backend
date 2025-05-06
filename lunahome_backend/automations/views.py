from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Automation
from .serializers import AutomationSerializer

class AutomationViewSet(viewsets.ModelViewSet):
    serializer_class = AutomationSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Automation.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def toggle(self, request, pk=None):
        automation = self.get_object()
        automation.is_active = not automation.is_active
        automation.save()
        serializer = self.get_serializer(automation)
        return Response(serializer.data)