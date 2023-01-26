from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .manager import CustomUserManager

class CustomUser(AbstractUser):
    username = None

    email = models.EmailField(_('email'), unique=True)
    first_name = models.CharField(_('first_name'), max_length=50)
    last_name = models.CharField(_('last_name'), max_length=50)

    USERNAME_FIELD  = 'email'

    REQUIRED_FIELDS = ['first_name']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'
