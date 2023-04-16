from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Patient, AlergyPatient
from .serializers import PatientSerializer, PatientAlergySerializer

# class PatientList(generics.ListCreateAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer


# class PatientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer


# class PatientAlergyListCreate(generics.ListCreateAPIView):
#     queryset = AlergyPatient.objects.all()
#     serializer_class = PatientAlergySerializer


# class PatientAlergyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = AlergyPatient.objects.all()
#     serializer_class = PatientAlergySerializer

class PatientView(APIView):

    def dispatch(self, request, *args, **kwargs):
        if request.method in ['GET', 'PUT', 'DELETE'] and 'pk' not in kwargs:
            return Response({'error': 'El campo pk es requerido para este metodo'}, status=status.HTTP_400_BAD_REQUEST)
        return super().dispatch(request, *args, **kwargs)
    
    
    def get_queryset(self, pk=None):
        if pk:
            return Patient.objects.filter(pk=pk)
        return Patient.objects.all()
    

    def get(self, request, pk=None):
        queryset = self.get_queryset(pk)
        many = True if pk else False
        serializer = PatientSerializer(queryset, many=many)
        return Response(serializer.data)

    

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        patient = self.get_queryset(pk).first()
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        patient = self.get_queryset(pk).first()
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class AlergyPatientView(APIView):


    def dispatch(self, request, *args, **kwargs):
        if request.method in ['GET', 'PUT', 'DELETE'] and 'pk' not in kwargs:
            return Response({'error': 'El campo pk es requerido para este metodo'}, status=status.HTTP_400_BAD_REQUEST)
        return super().dispatch(request, *args, **kwargs)
    

    def get_queryset(self, pk=None):
        if pk:
            return AlergyPatient.objects.filter(pk=pk)
        return AlergyPatient.objects.all()
    

    def get(self, request, pk=None):
        queryset = self.get_queryset(pk)
        many = True if pk else False
        serializer = PatientAlergySerializer(queryset, many=many)
        return Response(serializer.data)
    

    def post(self, request):
        patient_id = request.data.get('id_patient')
        alergies = request.data.get('alergy')

        if not alergies:
            return Response({'error': 'El campo alergias es requerido'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not isinstance(alergies, list):
            return Response({'error': 'El campo alergias debe ser una lista'}, status=status.HTTP_400_BAD_REQUEST)
        
        if len(alergies) != len(set(alergies)):
            return Response({'error': 'El campo alergias no debe tener elementos repetidos'}, status=status.HTTP_400_BAD_REQUEST)

        for alergy in alergies:
            serializer = PatientAlergySerializer(data={'id_patient': patient_id, 'alergy': alergy})
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({'message': 'Alergias agregadas correctamente'}, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        alergy_patient = self.get_queryset(pk).first()
        serializer = PatientAlergySerializer(alergy_patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        alergy_patient = self.get_queryset(pk).first()
        alergy_patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    




    




