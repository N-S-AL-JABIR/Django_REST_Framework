from django.contrib import admin
from . import models


@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "mobile_number", "fee")

    def full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    full_name.short_description = "Full Name"


@admin.register(models.Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Designation)
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(models.AvaliableTime)
admin.site.register(models.review)