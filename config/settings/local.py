from .base import *

# Development-specific settings
DEBUG = True

# Additional development apps
INSTALLED_APPS += [
    "django_extensions",  # if needed
]

# Development-specific middleware
# MIDDLEWARE += []

# Email backend for development
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
