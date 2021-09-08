from django.db import models

from django.contrib.auth.models import User

__all__ = (
    "Account",)


class Account(models.Model):
    """Linked to a user."""

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    password = models.TextField(max_length=100)
