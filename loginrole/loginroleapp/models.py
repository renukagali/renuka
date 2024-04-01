from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_user=models.BooleanField('is user',default=False)
    is_dealer=models.BooleanField('is dealer',default=False)
