from unicodedata import name

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import DoctorCreateAPIView, DoctorListAPI, DoctorDetailAPI

urlpatterns = [
    path("create/", DoctorCreateAPIView.as_view(), name="doctor-create"),
    path("", DoctorListAPI.as_view(), name="doctor-list"),
    path("<int:id>/", DoctorDetailAPI.as_view(), name="doctor-detail"),
]

#
# urlpatterns = router.urls

#
# path('specializations', SpecializationViewSet, name='specialization'),
#      path('', DoctorViewSet, name='doctor')
# ]
