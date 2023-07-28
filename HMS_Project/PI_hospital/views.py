from django.shortcuts import render, redirect

from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def homepage(request):
    return render(request, 'home.html')


def base(request):
    return render(request, 'base.html')


def aboutus(request):
    return render(request, 'about.html')


def contactus(request):
    return render(request, 'contact.html')


def contactus1(request):
    return render(request, 'contact1.html')


def loginpage(request):
    return render(request, 'adminpage.html')


@login_required(login_url='adminlogin')
def dashboard(request):
    doctors_count = Doctor.objects.count()
    patients_count = Patient.objects.count()
    pending_appointments_count = Appointment.objects.filter().count()

    context = {
        'doctors_count': doctors_count,
        'patients_count': patients_count,
        'appointments_count': pending_appointments_count
    }

    return render(request, 'dashboard.html', context)


# REGISTRATION

def admin_reg(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = AdminRegisterForm
        if request.method == 'POST':
            form = AdminRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, user + ' has been successfully registered as admin')
                return redirect('adminlogin')

    context = {'form': form}
    return render(request, 'adminregform.html', context)


# LOGIN

def admin_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username OR Password is Incorrect')
    context = {}
    return render(request, 'adminlogin.html', context)


def admin_logout(request):
    logout(request)
    # return redirect('home')
    return render(request, 'home.html')


# --------- To Render Doctoradd.html page -----------#
@login_required(login_url='adminlogin')
def doc_add(request):
    form = DoctorRegisterForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = DoctorRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            form = DoctorRegisterForm()
        return render(request, 'docotoradd.html', {'form': form})

    context = {'form': form}
    return render(request, 'docotoradd.html', context)


# --------- To Render Doctor view.html page -----------#
@login_required(login_url='adminlogin')
def doc_view(request):
    doctors = Doctor.objects.all()
    doccon = {'doctor': doctors}
    return render(request, 'doctorviews.html', doccon)


# --------- To Render Doctor Update.html page -----------#
@login_required(login_url='adminlogin')
def doc_update(request, pk):
    update_doc = Doctor.objects.get(Doctor_id=pk)
    form = DoctorUpdateForm(instance=update_doc)

    if request.method == 'POST':
        form = DoctorRegisterForm(request.POST, instance=update_doc)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            form = DoctorRegisterForm()
        return render(request, 'docotoradd.html', {'form': form})
    context = {'form': form}
    return render(request, 'docotoradd.html', context)


# --------- To Render Doctor Delete.html page -----------#
@login_required(login_url='adminlogin')
def doc_delete(request, pk):
    del_doc = Doctor.objects.get(Doctor_id=pk)
    print(del_doc)
    if request.method == "POST":
        del_doc.delete()
        return redirect('dashboard')
    else:
        context = {'item': del_doc}
        return render(request, 'doctordelete.html', context)


# --------- To Render Patient add.html page -----------#
@login_required(login_url='adminlogin')
def pat_add(request):
    form1 = PatientRegisterForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form1 = PatientRegisterForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('dashboard')
        else:
            form1 = PatientRegisterForm()
        return render(request, 'patientadd.html', {'form1': form1})

    context = {'form1': form1}
    return render(request, 'patientadd.html', context)


# --------- To Render Patient view.html page -----------#
@login_required(login_url='adminlogin')
def pat_view(request):
    patients = Patient.objects.all()

    pat_con = {'patient': patients}
    return render(request, 'patientview.html', pat_con)


# --------- To Render Patient Update.html page -----------#
@login_required(login_url='adminlogin')
def pat_update(request, pk):
    update_pat = Patient.objects.get(Patient_id=pk)
    form1 = PatientUpdateForm(instance=update_pat)

    if request.method == 'POST':
        form1 = PatientRegisterForm(request.POST, instance=update_pat)
        if form1.is_valid():
            form1.save()
            return redirect('dashboard')
        else:
            form1 = PatientRegisterForm()
        return render(request, 'patientadd.html', {'form1': form1})
    context = {'form1': form1}
    return render(request, 'patientadd.html', context)


# --------- To Render Patient Delete.html page -----------#
@login_required(login_url='adminlogin')
def pat_delete(request, pk):
    del_pat = Patient.objects.get(Patient_id=pk)
    print(del_pat)
    if request.method == "POST":
        del_pat.delete()
        return redirect('dashboard')

    else:
        context = {'item1': del_pat}
        return render(request, 'patientdelete.html', context)


# --------- To Render Appointment add.html page -----------#
@login_required(login_url='adminlogin')
def app_add(request):
    form2 = AppointmentForm()
    if request.method == 'POST':
        form2 = AppointmentForm(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('dashboard')
        else:
            form2 = AppointmentForm()
        return render(request, 'appointmentadd.html', {'form2': form2})

    context = {'form2': form2}
    return render(request, 'appointmentadd.html', context)


# --------- To Render Appointment view.html page -----------#
@login_required(login_url='adminlogin')
def app_view(request):
    appointments = Appointment.objects.all()
    app_con = {'appointment': appointments}
    return render(request, 'appointmentview.html', app_con)


# --------- To Render Appointment Update.html page -----------#
@login_required(login_url='adminlogin')
def app_update(request, pk):
    update_app = Appointment.objects.get(Appointment_id=pk)
    form2 = AppointmentUpdateForm(instance=update_app)

    if request.method == 'POST':
        form2 = AppointmentForm(request.POST, instance=update_app)
        if form2.is_valid():
            form2.save()
            return redirect('dashboard')
        else:
            form2 = AppointmentForm()
            appupcon = {'form2': form2}
        return render(request, 'appointmentadd.html', appupcon)
    context = {'form2': form2}
    return render(request, 'appointmentadd.html', context)


# --------- To Render Appointment Delete.html page -----------#
@login_required(login_url='adminlogin')
def app_delete(request, pk):
    del_app = Appointment.objects.get(Appointment_id=pk)
    if request.method == "POST":
        del_app.delete()

        return redirect('dashboard')
    context = {'item1': del_app}
    return render(request, 'appointmentdelete.html', context)


# --------- To Render Bill View.html page -----------#
from django.core.mail import send_mail


@login_required(login_url='adminlogin')
def calculate_total_bill(request):
    if request.method == 'POST':
        form = PatDischargeDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'billview.html', {'data': form.cleaned_data})
    else:
        form = PatDischargeDetailForm()

    return render(request, 'billcalculate.html', {'form': form})


##############################################################################################


from django.core.mail import send_mail
from .models import Pat_DischargeDetail


def send_bill_email(request, patient_email):
    # Fetch the bill data based on patient_email
    bill_data = Pat_DischargeDetail.objects.filter(Patient_email=patient_email)

    # Construct the email content
    email_subject = 'Your Bill Details'
    email_message = f"Dear Patient,\n\nPlease find below the details of your bill:\n\n"

    for bill in bill_data:
        email_message += f"Bill ID: {bill.pk}\n"
        email_message += f"Patient ID: {bill.Patient_id}\n"
        email_message += f"Patient Name: {bill.Patient_name}\n"
        email_message += f"Patient Email: {bill.Patient_email}\n"
        email_message += f'Doctor Name: {bill.Doctor_Name}\n'
        email_message += f'Patient Address: {bill.Patient_address}\n'
        email_message += f'Patient Mobile: {bill.Patient_mobile}\n'
        email_message += f'Patient Disease: {bill.Patient_disease}\n'
        email_message += f'Admit Date: {bill.Admit_Date}\n'
        email_message += f'Discharge Date: {bill.Discharge_Date}\n'
        email_message += f'Total Days: {bill.Total_days}\n'
        email_message += f'Room Charge: {bill.Room_Charge}\n'
        email_message += f'Medicine Cost: {bill.Medicine_Cost}\n'
        email_message += f'Doctor Fee: {bill.Doctor_Fee}\n'
        email_message += f'Other Charge: {bill.Other_Charge}\n'
        email_message += f'Total Bill Amount: {bill.Total_Bill_Amt}\n\n'

    email_message += "Thank you for choosing our hospital."

    # Send the email
    send_mail(
        subject=email_subject,
        message=email_message,
        from_email='pihms112@gmail.com',
        recipient_list=[patient_email],
        fail_silently=False
    )

    context = {'message': 'Email sent successfully!'}
    return render(request, 'billview.html', context)


