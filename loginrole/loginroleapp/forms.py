<<<<<<< HEAD
=======
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import User

# class LoginForm(forms.Form):
#     username = forms.CharField(
#         widget= forms.TextInput(
#             attrs={
#                 "class":"form-control"
#             }
#         )
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class":"form-control"
#             }
#         )
#     )
# class SignUpForm(UserCreationForm):
#     username = forms.CharField(
#         widget= forms.TextInput(
#             attrs={
#                 "class":"form-control"
#             }
#         )
#     )
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class":"form-control"
#             }
#         )
#     )
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class":"form-control"
#             }
#         )
#     )
#     email = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class":"form-control"
#             }
#         )
#     )

#     class Meta:
#         model = User
#         fields = ('Username','email','password1','password2','is_admin','is_user','is_dealer')
>>>>>>> 2595d271463a375dee563e2e8052274e8c599d87
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # Include fields as needed
class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password')