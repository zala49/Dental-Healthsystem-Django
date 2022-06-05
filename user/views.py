from django.contrib import messages
from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.views.generic import CreateView, FormView, View, TemplateView
from .models import User
from .forms import RegistrationForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from doctor.models import Doctor, Appointment
from django.http import HttpResponse

# Registration
class UserRegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        login(self.request, form.auth_user)
        return super(UserRegistrationView, self).form_valid(form)

# Login
class UserLoginView(FormView):
    form_class = LoginForm
    template_name = "user/login.html"
    success_url = reverse_lazy('home_index')

    def form_valid(self, form):
        login(self.request, form.auth_user)
        return super(UserLoginView, self).form_valid(form)

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out. ")
    return redirect('login')

# Home_index
class ShowIndexView(View):
    def get(self, request):
        doctor = Doctor.objects.all()
        context = {
            "doctor":doctor
        }
        return render(request,'index.html',context)
    
    def post(self,request):
        doctor = request.POST.get('doctor')
        start_date = request.POST.get('start-date')
        end_date = request.POST.get('end-date')
        problem = request.POST.get('problem')
        appointment = Appointment.objects.create(user=request.user,doctor_name=Doctor.objects.get(name=doctor),start_time=start_date,end_time =end_date,problem=problem)
        appointment.save()
        return HttpResponse("Your Appointment is Booked")