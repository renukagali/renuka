from django.contrib import admin
from . models import Product, Wishlist

# Register your models here.
admin.site.register(Product, Wishlist)