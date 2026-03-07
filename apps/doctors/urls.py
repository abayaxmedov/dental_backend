from unicodedata import name

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, SpecializationViewSet, DoctorCreateAPIView

# router = DefaultRouter()
# router.register('specializations', SpecializationViewSet, basename='specialization')
# router.register('', DoctorViewSet, basename='doctor')

urllpatterns =[
     path("create/", DoctorCreateAPIView.as_view(), name="doctor-create"),
     path('specializations', SpecializationViewSet, name='specialization'),
     path('', DoctorViewSet, name='doctor')
]
#
# urlpatterns = router.urls
