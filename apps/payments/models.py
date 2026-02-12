from django.db import models
from apps.base_model import BaseModel


class Payment(BaseModel):
    """Payment model for appointment payments."""
    
    PAYMENT_METHODS = [
        ('CARD', 'Credit/Debit Card'),
        ('CASH', 'Cash'),
        ('PAYME', 'Payme'),
        ('CLICK', 'Click'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    appointment = models.OneToOneField(
        'appointments.Appointment',
        on_delete=models.CASCADE,
        related_name='payment'
    )
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.amount} - {self.status}"
