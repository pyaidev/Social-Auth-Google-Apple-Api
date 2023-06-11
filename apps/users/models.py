from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedModel
from apps.users.managers import UserManager


# Create your models here.
class User(AbstractUser, TimeStampedModel):
    first_name = models.CharField(_("First name"), max_length=32, null=True, blank=True)
    last_name = models.CharField(_("Last name"), max_length=32, null=True, blank=True)
    full_name = models.CharField(_("Full name"), max_length=32, null=True, blank=True)
    bio = models.TextField(_("Bio"), null=True, blank=True)
    username = models.CharField(
        _("Username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        null=True,
        validators=[UnicodeUsernameValidator()],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    is_deleted = models.BooleanField(_("Is deleted"), default=False)
    email = models.EmailField(_("Email"), blank=True, null=True, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # type: ignore

    objects = UserManager()

    avatar = models.ImageField(upload_to="users/%Y/%m/", blank=True, null=True)

    def __str__(self):
        if self.email:
            return self.email
        if self.username:
            return self.username

    def prepare_to_delete(self):
        self.is_deleted = True
        for x in ["email", "username", "phone"]:
            if getattr(self, x):
                setattr(self, x, f"DELETED_{self.id}_{getattr(self, x)}")
        self.save()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
