from django import forms
from .models import User
from project1app.models import Product 

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'is_dealer']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']

# class WishlistForm(forms.ModelForm):
#     class Meta:
#         model = Wishlist
#         fields = ['product','price']
