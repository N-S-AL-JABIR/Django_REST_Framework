from django.contrib import admin
from . import models

@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("full_name", "date_of_birth", "gender", "mobile_number")

    def full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    full_name.short_description = "Full Name"
    
