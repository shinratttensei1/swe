from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('farmer', 'Farmer'),
        ('buyer', 'Buyer'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')
    is_approved = models.BooleanField(default=False)  # Farmers need approval
