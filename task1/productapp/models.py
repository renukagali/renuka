from django.db import models

#from django.contrib.auth.models import AbstractUser

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)


class Wishlist(models.Model):
    products = models.ManyToManyField(Product, related_name='wishlists')

    
    def __str__(self):
        return self.name
