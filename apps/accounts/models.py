from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from apps.base_model import BaseModel


class CustomUserManager(BaseUserManager):
    """Custom user manager for email/phone authentication."""
    
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Username is required')
        
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    """Custom user model with email and phone number support."""
    
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    
    # Profile fields
    user_image = models.ImageField(upload_to='users/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    
    # Location fields
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.username or f"User(pk={self.pk})"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username
