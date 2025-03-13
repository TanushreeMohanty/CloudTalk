from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Use CustomUser if you created a custom model

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser  # Change to User if using Django's default model
        fields = ['username', 'email', 'password1', 'password2']
