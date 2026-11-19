from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_CHOICES

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='patient/images/', null=True, blank=True)
    mobile_number = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    