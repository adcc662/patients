from rest_framework import serializers
from .models import Patient, AlergyPatient
from collections import Counter

class PatientAlergySerializer(serializers.ModelSerializer):
    class Meta:
        model = AlergyPatient
        fields = ('alergies',)

        

class PatientSerializer(serializers.ModelSerializer):
    alergies_all = PatientAlergySerializer(many=True, required=False)
    class Meta:
        model = Patient
        fields = ('name', 'sex', 'date_of_birth', 'direction', 'alergies_all')

    

    
    def to_representation(self, instance):
        # representation = {}
        # representation['name'] = instance.name
        # representation['sex'] = instance.sex
        # representation['date_of_birth'] = instance.date_of_birth
        # representation['direction'] = instance.direction
        representation = super().to_representation(instance)
        alergies_patients = AlergyPatient.objects.filter(patient=instance)
    
        representation['alergies_all'] = PatientAlergySerializer(alergies_patients, many=True).data
        return representation
    

    def create(self, validated_data):
        alergies_all = validated_data.pop('alergies_all')
        patient = Patient.objects.create(**validated_data)
        for alergy in alergies_all:
            AlergyPatient.objects.create(patient=patient, **alergy)
        return patient


    def validate(self, data):
            alergies_list = data.get('alergies_all', [])
            alergies_re = [alergy['alergies'] for alergy in alergies_list]
            duplicates = [item for item, count in Counter(alergies_re).items() if count > 1]
            if duplicates:
                raise serializers.ValidationError(f"Duplicated Alergies: {', '.join(duplicates)}")
            return data
    

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.direction = validated_data.get('direction', instance.direction)

        alergies_all = validated_data.pop('alergies_all')
        for alergy in alergies_all:
            alergy_patient = AlergyPatient.objects.get(patient=instance, alergies=alergy['alergies'])
            alergy_patient.alergies = alergy.get('alergies', alergy_patient.alergies)
            alergy_patient.save()

        instance.save()
        return instance

    

    
    
    

    

    