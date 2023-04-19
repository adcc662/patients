from django.db import models
import json
# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    date_of_birth = models.DateField(null=False, blank=False)
    direction = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name
    
class AlergyPatient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    alergies = models.TextField(default="[]")


    def get_alergies_list(self):
        return json.loads(self.alergies)
    

    def set_alergies_list(self, alergies_list):
        self.alergies = json.dumps(alergies_list)


    def __str__(self):
        return f"{self.patient}: {self.alergies}"
    
    


