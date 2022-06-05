from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    auth_user = None

    class Meta:
        model = User
        fields = ("email", "password1", "password2")
        
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# Login Form & Validation
class LoginForm(forms.Form):
    email = forms.EmailField()
    password= forms.CharField(widget=forms.PasswordInput())
    auth_user = None
    class Meta:
        model = User
    
    def clean(self):
        User = get_user_model()
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        print('password: ', password)
        if '.com' not in email:
            raise forms.ValidationError('Enter a valid Email')
        if len(password) < 4 :
            raise forms.ValidationError('Enter at least 4 Digits')
        self.auth_user = authenticate(
                username=User.objects.normalize_email(email),
                password=password,
            )
        if self.auth_user is None:
            raise forms.ValidationError('Information is wrong')
        return cleaned_data


