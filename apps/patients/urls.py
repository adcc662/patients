from django.urls import path
from .views import (
    PatientList,
    PatientRetrieveUpdateDestroy,
    PatientAlergyListCreate,
    PatientAlergyRetrieveUpdateDestroy,
)



urlpatterns = [
    path('patients/', PatientList.as_view(), name='patient_list_create'),
    path('patients/<int:pk>/', PatientRetrieveUpdateDestroy.as_view(), name='patient_retrieve_update_destroy'),
    path('patients-alergy/', PatientAlergyListCreate.as_view(), name='patient_alergy_list_create'),
    path('patients-alergy/<int:pk>/', PatientAlergyRetrieveUpdateDestroy.as_view(), name='patient_alergy_retrieve_update_destroy'),
]