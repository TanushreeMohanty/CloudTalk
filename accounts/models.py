from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):  # Extend AbstractUser
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Example extra field

    def __str__(self):
        return self.username
