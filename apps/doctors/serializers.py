from rest_framework import serializers
from .models import Doctor, Specialization
from apps.accounts.serializers import UserSerializer


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    specialization = SpecializationSerializer(read_only=True)
    specialization_id = serializers.PrimaryKeyRelatedField(
        queryset=Specialization.objects.all(),
        source='specialization',
        write_only=True
    )
    
    class Meta:
        model = Doctor
        fields = '__all__'




class DoctorCreateSerializer(serializers.ModelSerializer):
    specialization_id = serializers.PrimaryKeyRelatedField(
        queryset=Specialization.objects.all(),
        source="specialization",
        write_only=True
    )

    class Meta:
        model = Doctor
        fields = [
            "specialization_id",
            "hospital_name",
            "experience_years",
            "consultation_fee",
            "bio",
            "image"
        ]

    def create(self, validated_data):
        user = self.context["request"].user

        doctor = Doctor.objects.create(
            user=user,
            **validated_data
        )

        return doctor
