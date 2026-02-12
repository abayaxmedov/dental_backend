from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.user.get_full_name', read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'
