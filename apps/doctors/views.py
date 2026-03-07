from rest_framework import viewsets, filters, generics
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from apps.doctors.models import Doctor
from apps.doctors.serializers import DoctorSerializer, DoctorCreateSerializer

class DoctorListAPI(generics.ListAPIView):
    queryset = Doctor.objects.select_related(
        "user",
        "specialization"
    ).all()
    serializer_class = DoctorSerializer


class DoctorDetailAPI(generics.RetrieveAPIView):
    queryset = Doctor.objects.select_related(
        "user",
        "specialization"
    ).all()
    serializer_class = DoctorSerializer
    lookup_field = "id"

class DoctorCreateAPIView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorCreateSerializer
    permission_classes = [IsAuthenticated]
