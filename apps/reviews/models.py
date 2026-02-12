from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.base_model import BaseModel


class Review(BaseModel):
    """Review model for doctor ratings."""
    
    doctor = models.ForeignKey(
        'doctors.Doctor',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    patient = models.ForeignKey(
        'patients.Patient',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField()
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['doctor', 'patient']
    
    def __str__(self):
        return f"{self.rating} stars for {self.doctor}"
