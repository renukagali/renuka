from django import forms
from .models import User, Product, Wishlist
from django.contrib.auth.forms import PasswordChangeForm

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_dealer']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

class WishlistForm(forms.ModelForm):
  
    class Meta:
        model = Wishlist
        fields = []


# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name']

#     def _init_(self, *args, **kwargs):
#         super(UserProfileForm, self)._init_(*args, **kwargs)
#         self.fields['username'].disabled = True 

# class CustomPasswordChangeForm(PasswordChangeForm):
#     def _init_(self, *args, **kwargs):
#         super()._init_(*args, **kwargs)
#         self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Old Password'})
#         self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'New Password'})
#         self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm New Password'})