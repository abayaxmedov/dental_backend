from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Appointment
from .serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    """ViewSet for appointments."""
    
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'doctor', 'patient', 'date']
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Appointment.objects.all()
        
        # Show appointments for the current user (either as patient or doctor)
        queryset = Appointment.objects.none()
        
        if hasattr(user, 'patient_profile'):
            queryset |= Appointment.objects.filter(patient=user.patient_profile)
        
        if hasattr(user, 'doctor_profile'):
            queryset |= Appointment.objects.filter(doctor=user.doctor_profile)
        
        return queryset
