from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    # add additional fields in here
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.email