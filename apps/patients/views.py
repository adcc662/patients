from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError, ObjectDoesNotExist
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


class PatientList(APIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_object(self, pk=None):
        try:
            if pk is None:
                return self.queryset.all()
            return self.queryset.filter(id=pk)
        except Patient.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        
        serializer = PatientSerializer(self.get_object(pk), many=True)
        
        return Response(serializer.data)  
     

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, pk):
        patient = self.get_object(pk)
        if patient is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            print(patient.first())
            serializer = PatientSerializer(patient.first(), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        patient = self.get_object(pk)
        if patient is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
        



# class PatientDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Patient.objects.get(pk=pk)
#         except Patient.DoesNotExist:
#             raise Http404

    
#     def get(self, request, pk):
#         patient = self.get_object(pk)
#         serializer = PatientSerializer(patient)
#         return Response(serializer.data)
    

    
    
#     def put(self, request, pk):
#         patient = self.get_object(pk)
#         serializer = PatientSerializer(patient, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     def delete(self, request, pk):
#         patient = self.get_object(pk)
#         patient.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# class AlergyPatientList(APIView):
#     # def post(self, request):
#     #     serializer = PatientAlergySerializer(data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request):
#         alergies = AlergyPatient.objects.all()
#         serializer = PatientAlergySerializer(alergies, many=True)
#         return Response(serializer.data)


#     def post(self, request):
#         patient_id = request.data.get('patient_id')
#         alergies = request.data.get('alergies')

#         if not alergies:
#             return Response({"error": "Alergies list is empty"}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             patient = Patient.objects.get(id=patient_id)
#         except ObjectDoesNotExist:
#             return Response({"error": "Patient does not exist"}, status=status.HTTP_404_NOT_FOUND)

#         new_alergies = []
#         for alergy in alergies:
#             try:
#                 new_alergy = AlergyPatient(patient=patient, alergy=alergy)
#                 new_alergy.save()
#                 new_alergies.append(new_alergy)
#             except ValidationError as e:
#                 return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#         if new_alergies:
#             serializer = PatientAlergySerializer(new_alergies, many=True)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"error": "All alergies are already associated with the patient"}, status=status.HTTP_400_BAD_REQUEST)
    

# class AlergyPatientDetail(APIView):
    
#     def get_object(self, pk):
#         try:
#             return AlergyPatient.objects.get(pk=pk)
#         except AlergyPatient.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk):
#         alergy = self.get_object(pk)
#         serializer = PatientAlergySerializer(alergy)
#         return Response(serializer.data)
             
    
#     def put(self, request, pk):
#         alergy = self.get_object(pk)
#         serializer = PatientAlergySerializer(alergy, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     def delete(self, request, pk):
#         alergy = self.get_object(pk)
#         alergy.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

    




    




