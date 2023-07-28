from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Form for Admin Registration
class AdminRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


# Form for Admin Registration
class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

# Form for Doctor Registration
class DoctorRegisterForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


# Form for Doctor Updation
class DoctorUpdateForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


# Form for Patient Registration
class PatientRegisterForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


# Form for Patient Updation
class PatientUpdateForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


# Form for Appointments
class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


# Form for Appointments Update
class AppointmentUpdateForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


# Form for Patient Discharge Details
from django.core.mail import send_mail
class PatDischargeDetailForm(forms.ModelForm):
    class Meta:
        model = Pat_DischargeDetail
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        room_charge = cleaned_data.get('Room_Charge')
        medicine_cost = cleaned_data.get('Medicine_Cost')
        doctor_fee = cleaned_data.get('Doctor_Fee')
        other_charge = cleaned_data.get('Other_Charge')
        total_days = cleaned_data.get('Total_days')

        total_bill_amt = (room_charge + medicine_cost + doctor_fee + other_charge) * total_days
        cleaned_data['Total_Bill_Amt'] = total_bill_amt

        return cleaned_data


class EmailBillForm(forms.Form):
    patient_id = forms.IntegerField(label='Patient ID')

    def send_bill_email(self):
        patient_id = self.cleaned_data['patient_id']
        try:
            patient = Pat_DischargeDetail.objects.get(Patient_id=patient_id)
            send_bill_to_patient(patient)
            return True
        except Pat_DischargeDetail.DoesNotExist:
            return False
