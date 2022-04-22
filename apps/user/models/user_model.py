from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .user_manager import UserManager


class User(AbstractUser):
    username = None
    first_name = models.CharField(_('first name'), max_length=150, blank=False, null=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False, null=False)
    email = models.EmailField(_('email address'), unique=True, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
