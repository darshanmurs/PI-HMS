"""
URL configuration for HMS_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PI_hospital import views

urlpatterns = [

# Navigation Path Url's
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('home', views.homepage, name='homepage'),
    path('about', views.aboutus, name='about'),
    path('contact', views.contactus, name='contact'),
    path('contact1', views.contactus1, name='contact'),
    path('login', views.loginpage, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),

# Admin Related Pages
    path('adminreg', views.admin_reg, name='admin_reg'),
    path('adminlogin', views.admin_login, name='login'),
    path('adminlogout', views.admin_logout, name='logout'),


# Doctor Related pages
    path('docadd', views.doc_add, name='doc_add'),
    path('docviews', views.doc_view, name='doc_view'),
    path('docupdate/<str:pk>', views.doc_update, name='doc_up'),
    path('docdelete/<str:pk>', views.doc_delete, name='doc_del'),

# Patient Related Pages
    path('patadd', views.pat_add, name='pat_add'),
    path('patviews', views.pat_view, name='pat_view'),
    path('patupdate/<int:pk>', views.pat_update, name='pat_up'),
    path('patdelete/<int:pk>', views.pat_delete, name='pat_del'),

# Appointment Related Pages
    path('appadd', views.app_add, name='app_add'),
    path('appviews', views.app_view, name='app_view'),
    path('appupdate/<int:pk>', views.app_update, name='app_up'),
    path('appdelete/<int:pk>', views.app_delete, name='app_del'),

# Bill Calculations and Mailing Related Pages
    path('caltotalbill', views.calculate_total_bill, name='calculate_total_bill'),
    path('mailbill/<str:patient_email>/', views.send_bill_email, name='send_bill_email'),
    # path('mailbill/<int:pk>', views.send_bill_email, name='send_bill_email'),




    # path('doctorclick', views.doctorclick, name='doctorclick'),
    # path('patientclick', views.patientclick, name='patientclick'),
    # path('appointmentclick', views.appointmentclick, name='appointmentclick')

]
