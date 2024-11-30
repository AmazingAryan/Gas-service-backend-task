from django.db import models
from django.contrib.auth.models import AbstractUser

# Extend the user model
class User(AbstractUser):
    USER_TYPES = (
        ('customer', 'Customer'),
        ('staff', 'Staff'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

class ServiceRequest(models.Model):
    SERVICE_TYPES = (
        ('installation', 'Installation'),
        ('repair', 'Repair'),
        ('maintenance', 'Maintenance'),
    )
    STATUS_TYPES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('resolved', 'Resolved'),
    )
    service_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requests")
    type_of_service = models.CharField(max_length=20, choices=SERVICE_TYPES)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_TYPES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
