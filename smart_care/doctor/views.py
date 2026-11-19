from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer


class DesignationViewSet(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer


class AvailableTimeViewSet(viewsets.ModelViewSet):
    queryset = models.AvaliableTime.objects.all()
    serializer_class = serializers.AvaliableTimeSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.review.objects.all()
    serializer_class = serializers.reviewSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer


