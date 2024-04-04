from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        USERS = 'USERS', 'User'
        DEALER = 'DEALER', 'Dealer'

    is_dealer = models.BooleanField(default=False)
    role = models.CharField(max_length=6, choices=Role.choices, default=Role.USERS)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dealer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default='')


# class Wishlist(models.Model):
#     products = models.ManyToManyField(Product, related_name='wishlists')
#     price = models.DecimalField(max_digits=10, decimal_places=2)


#     def __str__(self):
#         return self.price