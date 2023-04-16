from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from apps.patients.models import Patient, AlergyPatient


class PatientTests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        response = self.client.post(reverse('token_obtain_pair'), {'username':'testuser', 'password':'12345'})
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {self.token}')

    def test_create_patient(self):
        
        data_patient = {
            'name': "Carlos Perez",
            'sex': 'M',
            'date_of_birth': '1990-01-01',
            'direction': 'Calle 1 # 2 - 3',
        }

        response = self.client.post(reverse('patient_list_create'), data_patient)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Patient.objects.count(), 1)
        self.assertEqual(Patient.objects.get().name, data_patient['name'])