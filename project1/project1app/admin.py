from django.contrib import admin
from .models import User, Product, Wishlist, Category

admin.site.register(User)
admin.site.register(Product)  
admin.site.register(Wishlist)  
admin.site.register(Category)
