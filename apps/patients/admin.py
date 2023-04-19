from django.contrib import admin

# Register your models here.

from .models import Patient, AlergyPatient

admin.site.register(Patient)
admin.site.register(AlergyPatient)