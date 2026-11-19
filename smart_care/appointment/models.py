from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvaliableTime

APOINTMENT_STATUS_CHOICES = [
    ("Pending", "Pending"),
    ("Scheduled", "Scheduled"),
    ("Completed", "Completed"),
    ("Running", "Running"),
]
APOINTMENT_TYPE_CHOICES = [
    ("Online", "Online"),
    ("Offline", "Offline"),
]
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_status = models.CharField(
        max_length=10, choices=APOINTMENT_STATUS_CHOICES, default="Pending"
    )
    appointment_type = models.CharField(max_length=10, choices=APOINTMENT_TYPE_CHOICES, default="Offline")
    symptoms = models.TextField()
    time = models.ForeignKey(AvaliableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Doctor: {self.doctor.user.last_name} Patient: {self.patient.user.first_name} at {self.time}"
