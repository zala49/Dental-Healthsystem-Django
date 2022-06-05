from django.contrib import admin
from .models import Appointment, Doctor


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id','user','doctor_name','problem','start_time','end_time']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id','name']