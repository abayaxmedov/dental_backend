# URL configuration for all apps
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('apps.accounts.urls')),
    path('doctors/', include('apps.doctors.urls')),
    path('patients/', include('apps.patients.urls')),
    path('appointments/', include('apps.appointments.urls')),
    path('reviews/', include('apps.reviews.urls')),
    path('payments/', include('apps.payments.urls')),
]
