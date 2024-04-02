from django import forms
from task1app.models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User  
        fields = ['username', 'password', 'email','role']  
        

class DealerRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'role']