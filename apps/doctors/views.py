from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Doctor, Specialization
from .serializers import DoctorSerializer, SpecializationSerializer


class SpecializationViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for viewing specializations."""
    
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class DoctorViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for viewing doctors."""
    
    queryset = Doctor.objects.filter(is_available=True)
    serializer_class = DoctorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['specialization', 'is_available']
    search_fields = ['user__first_name', 'user__last_name', 'hospital_name']
    ordering_fields = ['rating', 'experience_years', 'consultation_fee']
