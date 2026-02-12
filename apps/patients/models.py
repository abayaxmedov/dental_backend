from django.db import models
from django.conf import settings
from apps.base_model import BaseModel


class Patient(BaseModel):
    """Patient profile linked to CustomUser."""
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='patient_profile'
    )
    
    # Medical info
    blood_type = models.CharField(max_length=5, blank=True)
    allergies = models.TextField(blank=True)
    medical_history = models.TextField(blank=True)
    
    # Contact
    emergency_contact = models.CharField(max_length=15, blank=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    
    # Profile
    image = models.ImageField(upload_to='patients/', blank=True, null=True)
    
    def __str__(self):
        return self.user.get_full_name()
    
    class Meta:
        ordering = ['-created_at']
