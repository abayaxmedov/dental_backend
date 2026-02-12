import os
from decouple import config

# Default to local settings
ENVIRONMENT = config("ENVIRONMENT", default="local")

if ENVIRONMENT == "production":
    from .production import *
else:
    from .local import *
