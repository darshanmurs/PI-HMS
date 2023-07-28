from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
# Array that represents doctor Specialization

Spcl = [('Cardiologist', 'Cardiologist'), ('Dermatologist', 'Dermatologist'), ('Anesthesiologists', 'Anesthesiologists')
    , ('Surgeons', 'Surgeons'), ('Critical Care Medicine Specialists', 'Critical Care Medicine Specialists'),
        ('Endocrinologists', 'Endocrinologists'), ('Gastroenterologists', 'Gastroenterologists'), ('Pediatricians',
                                                                                                   'Pediatricians'),
        ('Neurologists', 'Neurologists'), ('Psychiatrists', 'Psychiatrists'),
        ('General Surgeons', 'General Surgeons')]


# Doctors Model
class Doctor(models.Model):
    Doctor_id = models.IntegerField(primary_key=True)
    Doctor_name = models.CharField(max_length=50)
    Doctor_gender = models.CharField(max_length=10)
    Doctor_email = models.EmailField(max_length=30)
    Doctor_mobile = models.IntegerField(null=False)
    Doctor_specialization = models.CharField(max_length=50, choices=Spcl, default='')
    Doctor_address = models.CharField(max_length=250)

    def __int__(self):
        return self.Doctor_id


# Patients Model
class Patient(models.Model):
    Patient_id = models.IntegerField(primary_key=True)
    Patient_name = models.CharField(max_length=40)
    Patient_email = models.EmailField(max_length=30)
    Patient_gender = models.CharField(max_length=10)
    Patient_mobile = models.IntegerField(null=False)
    Patient_address = models.CharField(max_length=250)
    Patient_disease = models.CharField(max_length=50)
    Doctor_idAssign = models.ForeignKey(Doctor, null=True, on_delete=models.CASCADE)
    Admit_Date = models.DateField(auto_now=True)


    def __int__(self):
        return self.Patient_id


# Appointments Model

App_status = [('Pending', 'Pending'), ('Approved', 'Approved')
              ]


class Appointment(models.Model):
    Patient_id = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE)
    Patient_name = models.CharField(max_length=40)
    Doctor_id = models.ForeignKey(Doctor, null=True, on_delete=models.CASCADE)
    Doctor_name = models.CharField(max_length=50)
    Description = models.TextField(max_length=500)
    Appointment_id = models.IntegerField(primary_key=True)
    Appointment_Date = models.DateField(auto_now=True)
    App_Confirmation = models.CharField(max_length=50, choices=App_status, default='')

    def __int__(self):
        return self.Appointment_id


# Discharge Model
class Pat_DischargeDetail(models.Model):
    Patient_id = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE)
    Patient_name = models.CharField(max_length=30)
    Patient_email = models.EmailField(max_length=30, default="")
    Doctor_Name = models.CharField(max_length=40)
    Patient_address = models.CharField(max_length=40)
    Patient_mobile = models.CharField(max_length=20, null=True)
    Patient_disease = models.CharField(max_length=100, null=True)

    Admit_Date = models.DateField(null=False)
    Discharge_Date = models.DateField(null=False)
    Total_days = models.PositiveIntegerField(null=False)

    Room_Charge = models.PositiveIntegerField(null=False)
    Medicine_Cost = models.PositiveIntegerField(null=False)
    Doctor_Fee = models.PositiveIntegerField(null=False)
    Other_Charge = models.PositiveIntegerField(null=False)
    Total_Bill_Amt = models.PositiveIntegerField(null=False)

    def __int__(self):
        return self.Patient_id

