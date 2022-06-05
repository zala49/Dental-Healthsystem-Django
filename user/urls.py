from django.urls import path
from .views import UserRegistrationView, UserLoginView, ShowIndexView
from user import views

urlpatterns = [
    path('register/',UserRegistrationView.as_view(), name='register'),
    path('home/', ShowIndexView.as_view(), name='home_index'),
    path('logout/', views.logout_request, name='logout'),
    path('', UserLoginView.as_view(), name='login'),
]
