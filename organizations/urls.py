from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views
# router.register('category', CategoryViewSet)
'''
Organization
WorkHour
Specialization
Professional
Feedback
Appointment
'''

router = SimpleRouter()
router.register('organization', views.OrganizationView)
router.register('workhour', views.WorkHourView)
router.register('specialization', views.SpecializationView)
router.register('professional', views.ProfessionalView)
router.register('feedback', views.FeedbackView)
router.register('appointment', views.AppointmentView)

urlpatterns = router.urls