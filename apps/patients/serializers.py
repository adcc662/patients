from rest_framework import serializers
from .models import Patient, AlergyPatient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class PatientAlergySerializer(serializers.ModelSerializer):
    class Meta:
        model = AlergyPatient
        fields = '__all__'