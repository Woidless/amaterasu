from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .permissions import IsAuthor
from . import serializers, models


class OrganizationView(ModelViewSet):
    permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly, IsAuthor)
    serializer_class = serializers.OrganizationSerializer
    queryset = models.Organization.objects.all()


class WorkHourView(ModelViewSet):
    permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly, IsAuthor)
    serializer_class = serializers.WorkHourSerializer
    queryset = models.WorkHour.objects.all()


class SpecializationView(ModelViewSet):
    permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly, IsAuthor)
    serializer_class = serializers.SpecializationSerializer
    queryset = models.Specialization.objects.all()


class ProfessionalView(ModelViewSet):
    permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly, IsAuthor)
    serializer_class = serializers.ProfessionalSerializer
    queryset = models.Professional.objects.all()


class FeedbackView(ModelViewSet):
    permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly, IsAuthor)
    serializer_class = serializers.FeedbackSerializer
    queryset = models.Feedback.objects.all()


class AppointmentView(ModelViewSet):
    permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly, IsAuthor)
    serializer_class = serializers.AppointmentSerializer
    queryset = models.Appointment.objects.all()


