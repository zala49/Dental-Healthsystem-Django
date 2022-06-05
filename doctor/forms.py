from django import forms
from .models import Appointment

class CreteAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"
