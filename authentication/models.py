from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.db import models


# Create your models here.
class User(AbstractUser):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True
    )
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(blank=True, null=True, max_length=255)
    mobile_number = models.CharField(max_length=15, null=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.email)

    def set_password(self, password):
        self.password = password
