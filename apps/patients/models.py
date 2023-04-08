from django.db import models

# Create your models here.

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    date_of_birth = models.DateField()
    direction = models.TextField()

    def __str__(self):
        return self.name
    
class AlergyPatient(models.Model):
    id = models.AutoField(primary_key=True)
    id_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    alergy = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id_patient}: {self.alergy}"
    
    


