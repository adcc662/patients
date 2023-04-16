from django.urls import path
from .views import (
    PatientView,
    AlergyPatientView

)



urlpatterns = [
    path('patients/', PatientView.as_view(), name='patients'),
    path('patients/<int:pk>/', PatientView.as_view(), name='patient-detail'),
    path('patients-alergy/', AlergyPatientView.as_view(), name='alergy_patients'),
    path('patients-alergy/<int:pk>/', AlergyPatientView.as_view(), name='alergy_patients-detail'),
]