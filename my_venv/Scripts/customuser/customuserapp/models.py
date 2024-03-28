from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomAccountManager(BaseUserManager):
   
    def create_superuser(self, email, username, password):
        # Call the parent class method to create a superuser
        user = self.create_user(email, username=username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return super
    

    def create_user(self, email, username, password):
        if not email:
            raise ValueError("You must provide an email address.")

        
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save()
        return user

       

class NewUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomAccountManager()
