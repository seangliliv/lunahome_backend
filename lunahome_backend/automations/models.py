from django.db import models
import uuid
from users.models import User

class Automation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='automations')
    is_active = models.BooleanField(default=True)
    trigger_data = models.JSONField()
    condition_data = models.JSONField(blank=True, null=True)
    action_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name