from django.db import models
from apps.base_model import BaseModel


class Appointment(BaseModel):
    """Appointment model for booking doctor visits."""
    
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    doctor = models.ForeignKey(
        'doctors.Doctor',
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    patient = models.ForeignKey(
        'patients.Patient',
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-date', '-time']
        unique_together = ['doctor', 'date', 'time']
    
    def __str__(self):
        return f"{self.patient} with {self.doctor} on {self.date} at {self.time}"
