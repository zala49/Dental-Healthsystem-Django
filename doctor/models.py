from django.db import models
from django.urls import reverse
from user.models import User
import datetime


class Doctor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_name = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True) 
    start_time = models.TimeField(default=datetime.datetime.now)
    end_time = models.TimeField(default= datetime.datetime.now)
    problem = models.TextField(null=True)

    def __str__(self):
        return self.doctor_name.name
