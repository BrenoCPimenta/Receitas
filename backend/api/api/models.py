"""Modules.
"""
from django.db import models

class User(models.Model):
    """User model.
    """
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=50)