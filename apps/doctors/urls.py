from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, SpecializationViewSet

router = DefaultRouter()
router.register('specializations', SpecializationViewSet, basename='specialization')
router.register('', DoctorViewSet, basename='doctor')

urlpatterns = router.urls
