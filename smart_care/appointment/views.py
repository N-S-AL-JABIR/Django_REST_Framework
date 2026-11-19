from django.shortcuts import render
from rest_framework import viewsets
from . import models
from .serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        patient_id = self.request.query_params.get("patient_id")
        doctor_id = self.request.query_params.get("doctor_id")
        if patient_id:
            queryset = queryset.filter(patient__id=patient_id)
        if doctor_id:
            queryset = queryset.filter(doctor__id=doctor_id)
        return queryset