from django import forms
from productapp.models import Product, Wishlist


class ProductInfo(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = []