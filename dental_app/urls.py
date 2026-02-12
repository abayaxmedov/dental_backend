from django.urls import path
from .views import (
    DoctorViewSet, SpecializationViewSet, PatientViewSet,
    AppointmentViewSet, ReviewViewSet, PaymentViewSet,
    RegisterView, LoginView
)

urlpatterns = [
    # Authentication
    path('auth/signup/', RegisterView.as_view(), name='sign-up'),
    path('auth/signin/', LoginView.as_view(), name='sign-in'),

    # Specializations
    path('specializations/', SpecializationViewSet.as_view({'get': 'list', 'post': 'create'}), name='specialization-list'),
    path('specializations/<int:pk>/', SpecializationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='specialization-detail'),

    # Doctors
    path('doctors/', DoctorViewSet.as_view({'get': 'list', 'post': 'create'}), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='doctor-detail'),

    # Patients
    path('patients/', PatientViewSet.as_view({'get': 'list', 'post': 'create'}), name='patient-list'),
    path('patients/<int:pk>/', PatientViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='patient-detail'),

    # Appointments
    path('appointments/', AppointmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='appointment-list'),
    path('appointments/<int:pk>/', AppointmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='appointment-detail'),

    # Reviews
    path('reviews/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review-list'),
    path('reviews/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='review-detail'),

    # Payments
    path('payments/', PaymentViewSet.as_view({'get': 'list', 'post': 'create'}), name='payment-list'),
    path('payments/<int:pk>/', PaymentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='payment-detail'),
]

