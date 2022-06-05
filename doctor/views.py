from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, View
from django.shortcuts import render
from doctor.models import Appointment,Doctor


class ContactInfo(TemplateView):
    """
    show contact template
    """
    template_name = 'contact.html'


class ErrorShow(TemplateView):
    """
    show 404 Error page
    """
    template_name = '404.html'


class Team(TemplateView):
    """Show Team Page"""

    template_name = 'team.html'


class Feature(TemplateView):
    template_name = 'feature.html'


class Service(TemplateView):
    template_name = 'service.html'


class About(TemplateView):
    template_name = 'about.html'


class AppointmentCreate(View):
    def get(self, request):
        doctor = Doctor.objects.all()
        context = {
            "doctor":doctor
        }
        return render(request,'appointment_form.html',context)
    
    def post(self,request):
        doctor = request.POST.get('doctor')
        start_date = request.POST.get('start-date')
        end_date = request.POST.get('end-date')
        problem = request.POST.get('problem')

        appointment = Appointment.objects.create(user=request.user,doctor_name=Doctor.objects.get(name=doctor),start_time=start_date,end_time =end_date,problem=problem)
        appointment.save()
        return HttpResponse("Your Appointment is Booked")
