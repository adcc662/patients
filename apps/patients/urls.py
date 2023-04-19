from django.urls import path
from .views import (
    PatientList,
    

)



urlpatterns = [
    path('patients/', PatientList.as_view(), name='patients'),
    path('patients/<int:pk>/', PatientList.as_view(), name='patient-detail'),
    path('patients-alergy/', PatientList.as_view(), name='alergy_patients'),
    # path('patients-alergy/<int:pk>/', AlergyPatientDetail.as_view(), name='alergy_patients-detail'),
]