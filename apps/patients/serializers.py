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

    def validate(self, data):
        if data['id_patient'] == data['alergy']:
            raise serializers.ValidationError("The patient can't have the same alergy")
        return data
    