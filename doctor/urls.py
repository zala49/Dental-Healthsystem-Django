from django.urls import path
from .views import AppointmentCreate,ContactInfo, ErrorShow, Team, Feature, Service, About


urlpatterns = [
    path('contact/',ContactInfo.as_view(), name='contact'),
    path('error/',ErrorShow.as_view(), name='error'),
    path('team/',Team.as_view(), name='team'),
    path('feature/',Feature.as_view(), name='feature'),
    path('service/',Service.as_view(), name='service'),
    path('about/',About.as_view(), name='about'),
    path('appointment/',AppointmentCreate.as_view(), name='appointmentcreate'),
]
