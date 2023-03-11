from django.db import models
from django.utils.translation import gettext as _

class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    longtitude = models.FloatField()
    latitude = models.FloatField()
    website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)


class WorkHour(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    WEEKDAYS = [
        (1, _("Monday")),
        (2, _("Tuesday")),
        (3, _("Wednesday")),
        (4, _("Thursday")),
        (5, _("Friday")),
        (6, _("Saturday")),
        (7, _("Sunday")),
    ]

    weekday = models.IntegerField(choices=WEEKDAYS)
    open_hour = models.TimeField()
    close_hour = models.TimeField()


class Specialization(models.Model):
    name = models.CharField(max_length=255)
    descprition = models.TextField()
    

class Professional(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=20)
    information = models.TextField()


class Feedback(models.Model):
    user = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE)
    professional = models.ForeignKey(Professional, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    

class Appointment(models.Model):
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    user = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE)
    begin_time = models.DateTimeField()
    duration = models.DurationField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField()
    is_past = models.BooleanField()