from rest_framework import serializers
from . import models


class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    specialization = serializers.PrimaryKeyRelatedField(
        queryset=models.Specialization.objects.all(), many=True, write_only=True
    )
    specializations = serializers.StringRelatedField(
        many=True, source="specialization", read_only=True
    )

    designation = serializers.PrimaryKeyRelatedField(
        queryset=models.Designation.objects.all(), many=True, write_only=True
    )
    designations = serializers.StringRelatedField(
        many=True, source="designation", read_only=True
    )
    available_time = serializers.PrimaryKeyRelatedField(
        queryset=models.AvaliableTime.objects.all(), many=True, write_only=True
    )
    available_times = serializers.StringRelatedField(
        many=True, source="available_time", read_only=True
    )

    class Meta:
        model = models.Doctor
        fields = "__all__"


class SpecializationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Specialization
        fields = "__all__"


class DesignationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Designation
        fields = "__all__"


class AvaliableTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AvaliableTime
        fields = "__all__"


class reviewSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(
        queryset=models.Doctor.objects.all(), many=False, write_only=True)
    doctor_name = serializers.StringRelatedField(many=False, read_only=True,source='doctor')
    patient = serializers.PrimaryKeyRelatedField(
        queryset=models.Patient.objects.all(), many=False, write_only=True)
    patient_name = serializers.StringRelatedField(many=False, read_only=True,source='patient.user')

    class Meta:
        model = models.review
        fields = "__all__"
