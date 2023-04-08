from django.shortcuts import render
from rest_framework import generics
from .models import Patient, AlergyPatient
from .serializers import PatientSerializer, PatientAlergySerializer

class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientAlergyListCreate(generics.ListCreateAPIView):
    queryset = AlergyPatient.objects.all()
    serializer_class = PatientAlergySerializer


class PatientAlergyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlergyPatient.objects.all()
    serializer_class = PatientAlergySerializer
