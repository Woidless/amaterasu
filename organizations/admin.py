from django.contrib import admin

from .models import (
    Organization,
    Specialization,
    Appointment,
    Feedback,
    Professional,
    WorkHour,
)

admin.site.register(Organization)
admin.site.register(Specialization)
admin.site.register(Appointment)
admin.site.register(Feedback)
admin.site.register(Professional)
admin.site.register(WorkHour)