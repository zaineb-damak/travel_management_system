from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(_('email address'), blank=False)

    def save(self, *args, **kwargs):
          self.set_password(self.password)
          super().save(*args, **kwargs)
   
    def __str__(self):
        return self.username


