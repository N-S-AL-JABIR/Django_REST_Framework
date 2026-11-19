from django.shortcuts import render
from rest_framework import viewsets
from .models import Service
from .serializers import ServicesSerializer


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer