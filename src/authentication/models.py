from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Modelo personalizado de usuario extendiendo el usuario base de Django"""
    phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)