from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission, Group
from django.db import models

class AccountManager(BaseUserManager):
    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, username, password, **extra_fields)

    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
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
    REQUIRED_FIELDS = ['email', 'username']

    objects = AccountManager()

    def __str__(self):
        return self.username
