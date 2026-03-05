from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.accounts.models import CustomUser

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user data."""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'first_name', 'last_name', 'user_image']
        read_only_fields = ['id']


class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password', 'password_confirm', 
                  'first_name', 'last_name']
    
    def validate(self, attrs):

        if attrs.get('password') != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        attrs.pop('password_confirm')
        return attrs
    
    def create(self, validated_data):
        password = validated_data.pop("password")

        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["username"] = user.username
        token["email"] = user.email

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = UserSerializer(self.user).data
        data["access"] = str(data["access"])
        data["refresh"] = str(data["refresh"])
        return data