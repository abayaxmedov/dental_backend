from django.db import models
from django.conf import settings
from apps.base_model import BaseModel


class Specialization(BaseModel):
    """Medical specialization for doctors."""
    
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='specializations/', blank=True, null=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Doctor(BaseModel):
    """Doctor profile linked to CustomUser."""
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='doctor_profile'
    )
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.SET_NULL,
        null=True,
        related_name='doctors'
    )
    
    # Professional info
    hospital_name = models.CharField(max_length=200)
    experience_years = models.IntegerField(default=0)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Stats
    rating = models.FloatField(default=0.0)
    patients_count = models.IntegerField(default=0)
    
    # Additional info
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='doctors/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Dr. {self.user.get_full_name()}"
    
    class Meta:
        ordering = ['-rating', '-patients_count']
