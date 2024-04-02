<<<<<<< HEAD
=======
# loginroleapp/models.py
>>>>>>> 2595d271463a375dee563e2e8052274e8c599d87

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add fields as needed
    is_users = models.BooleanField(default=False)
    is_dealer = models.BooleanField(default=False)
<<<<<<< HEAD
   
=======
    is_admin = models.BooleanField(default=False)
>>>>>>> 2595d271463a375dee563e2e8052274e8c599d87
