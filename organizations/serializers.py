from rest_framework import serializers

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from . import models

User = get_user_model()


class OrganizationSerializer(serializers.Serializer):
    class Meta:
        model = models.Organization
        fields = '__all__'


class WorkHourSerializer(serializers.Serializer):
    class Meta:
        model = models.WorkHour
        fields = '__all__'


class SpecializationSerializer(serializers.Serializer):
    class Meta:
        model = models.Specialization
        fields = '__all__'




class ProfessionalSerializer(serializers.Serializer):
    class Meta:
        model = models.Professional
        fields = '__all__'


class FeedbackSerializer(serializers.Serializer):
    class Meta:
        model = models.Feedback
        fields = '__all__'


class AppointmentSerializer(serializers.Serializer):
    class Meta:
        model = models.Appointment
        fields = '__all__'
