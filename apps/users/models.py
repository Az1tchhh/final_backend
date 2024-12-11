from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.managers import UserManager
from apps.utils.models import TimeStampMixin, AbstractModel


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    username = models.CharField(max_length=255, unique=True)

    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self):
        return self.username if self.username else self.pk


class WebUser(AbstractModel, TimeStampMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='web_user')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)