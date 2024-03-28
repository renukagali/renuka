from django.contrib.auth.models import AbstractUser, BaseUserManager,Permission,Group
from django.db import models

class AccountManager(BaseUserManager):
    def create_superuser(self, email, username, password):
        user = self.create_user(email, username=username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("You must provide an email address.")
        
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

class Dealer(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    groups = models.ManyToManyField(Group, blank=True, related_name='dealer_groups')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='dealer_user_permissions')

   
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['company_name']
    
    objects = AccountManager()

