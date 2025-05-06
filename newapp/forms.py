from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'number', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
