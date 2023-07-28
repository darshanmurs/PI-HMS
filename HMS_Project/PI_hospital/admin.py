from django.contrib import admin
from PI_hospital.models import *

# Admin can Register DOCTORS, PATIENTS and APPOINTMENTS


admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Pat_DischargeDetail)
