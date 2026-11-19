from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient_name", "doctor_name", "appointment_status","symptoms", "appointment_type", "time", "cancel")

    def patient_name(self, obj):
        return f"{obj.patient.user.first_name} {obj.patient.user.last_name}"

    def doctor_name(self, obj):
        return f"{obj.doctor.user.first_name} {obj.doctor.user.last_name}"

    patient_name.short_description = "Patient Name"
    doctor_name.short_description = "Doctor Name"
    