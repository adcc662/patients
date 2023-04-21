from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from apps.patients.models import Patient, AlergyPatient


class PatientTests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        response = self.client.post(reverse('token_obtain_pair'), {'username':'test', 'password':'test'})
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {self.token}')

        
      

        # self.patient = Patient.objects.create(
        #     name='Juan Perez',
        #     sex='M',
        #     date_of_birth='1985-05-05',
        #     direction='Calle 5 # 10 - 15'
        # )
        # self.alergy1 = AlergyPatient.objects.create(
        #     patient=self.patient,
        #     alergies='alergia3'
        # )
        # self.alergy2 = AlergyPatient.objects.create(
        #     patient=self.patient,
        #     alergies='alergia4'
        # )

        # response = self.client.post(reverse('patients'), self.data_patient)

        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Patient.objects.count(), 1)
        # self.assertEqual(Patient.objects.get().name, self.data_patient['name'])

    def test_create_patient(self):
        patient = {
            'name': "Carlos Perez",
            'sex': 'M',
            'date_of_birth': '1990-01-01',
            'direction': 'Calle 1 # 2 - 3',
            "alergies_all": [
       {"alergies": "Chocolate"},
       {"alergies": "Manzana"},
       {"alergies": "Carne"}

    ]
            
        }
        response = self.client.post(reverse('patients'), patient)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        # created_patient = Patient.objects.get(pk=response.data['pk'])
        self.assertEqual(Patient.objects.count(), 1)
        self.assertEqual(Patient.objects.get().name, patient['name'])

    
    def test_get_patient_list(self):
        patient_2 = {
            'name': "Carlos Perez",
            'sex': 'M',
            'date_of_birth': '1990-01-01',
            'direction': 'Calle 1 # 2 - 3',
            "alergies_all": [
       {"alergies": "Chocolate"},
       {"alergies": "Manzana"},
       {"alergies": "Carne"}

    ]          
        }
        response = self.client.get(reverse('patients'), patient_2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    
    def test_get_single_patient(self):
        patient = {
            'name': "Carlos Perez",
            'sex': 'M',
            'date_of_birth': '1990-01-01',
            'direction': 'Calle 1 # 2 - 3',
            "alergies_all": [
       {"alergies": "Chocolate"},
       {"alergies": "Manzana"},
       {"alergies": "Carne"}

            ]
            
        }
        response = self.client.post(reverse('patients'), patient)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        created_patient = Patient.objects.get(name=response.data['name'])
        response = self.client.get(reverse('patient-detail', kwargs={'pk':created_patient.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    
    def test_update_patient(self):
        patient = {
            'name': "Juan Carlos",
            'sex': 'M',
            'date_of_birth': '1990-01-01',
            'direction': 'Calle 1 # 2 - 3',
            "alergies_all": [
       {"alergies": "Chocolate"},
       {"alergies": "Manzana"},
       {"alergies": "Carne"}

                ]
            
                }
        response = self.client.post(reverse('patients'), patient)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        created_patient = Patient.objects.get(name=response.data['name'])
        patient['name'] = 'Carlos Perez'
        print(patient)
        response = self.client.put(reverse('patient-detail', kwargs={'pk':created_patient.pk}), patient)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('Carlos Perez', response.data['name'])
        total_alergias = AlergyPatient.objects.filter(patient=created_patient).count()
        self.assertEqual(total_alergias, 3)



    
    def test_delete_patient(self):
        patient = {
            'name': "Carlos Perez",
            'sex': 'M',
            'date_of_birth': '1990-01-01',
            'direction': 'Calle 1 # 2 - 3',
            "alergies_all": [
       {"alergies": "Chocolate"},
       {"alergies": "Manzana"},
       {"alergies": "Carne"}

    ]
            
        }
        response = self.client.post(reverse('patients'), patient)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        created_patient = Patient.objects.get(name=response.data['name'])
        response = self.client.delete(reverse('patient-detail', kwargs={'pk':created_patient.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Patient.objects.count(), 0)
        

    


    


        
        
