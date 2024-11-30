from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, ServiceRequest

class CustomerRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'city', 'address']

class StaffRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'city']

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['type_of_service', 'description', 'attachment']
