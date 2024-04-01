# loginroleapp/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add fields as needed
    is_users = models.BooleanField(default=False)
    is_dealer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
