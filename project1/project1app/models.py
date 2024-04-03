from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_dealer = models.BooleanField(default=False)
    class Role(models.TextChoices):
        USERS = 'users', 'Users'
        DEALER = 'dealer', 'Dealer'
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.USERS)    

    def _str_(self):
        return self.username
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

# class Wishlist(models.Model):
#     products = models.ManyToManyField(Product, related_name='wishlists')
#     price = models.DecimalField(max_digits=10, decimal_places=2)


#     def __str__(self):
#         return f"{self.user.username}'s wishlist: {self.product.name}"
